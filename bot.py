import os
import json
from time import sleep
import requests
from dotenv import load_dotenv
from api import Api

load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")


class Bot ():
    """ Telegram bot """

    def __init__(self):
        self.token = BOT_TOKEN
        self.url = f"https://api.telegram.org/bot{self.token}"

    def send_message(self, chat_id: int, text: str):
        """ Send message to specified chat

        Args:
            chat_id (int): id of the chat with user
            text (str): text of the message
            bot_token (str): token of the bot
        """

        print(f"Sending message to {chat_id}: {text}")

        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": text,
        }
        json_data = json.dumps(data)
        headers = {
            "Content-Type": "application/json"
        }
        res = requests.post(url, data=json_data, headers=headers)
        res.raise_for_status()

    def workflow(self, message: str, chat_id: int, bot_name: str):
        """ Main bot workflow (get and send message)

        Args:
            message (str): message send by user
            chat_id (int): id of the chat with user
            bot_name (str): name of the bot in database
        """

        welcome_message = "Enter your product keyword to compare prices " \
            "on Amazon, eBay, and Walmart:"
        wait_message = "We are obtaining the real-time prices for you "\
            "right now. The process might take around 2 minutes! Hold on!"
        error_message = "Sorry, telegram is not working properly. " \
            "Try again later."
        preview_message = "Grab here your comparative " \
            "(ultra-safe link 🔒): \n\n"

        if message in ["/start", "/info"]:
            # Send info message
            self.send_message(chat_id, welcome_message)
        else:
            # Send waiting message
            self.send_message(chat_id, wait_message)

            # Connect with api
            api = Api(keyword=message)
            keyword_sent = api.post_keyword()
            if not keyword_sent:
                self.send_message(chat_id, error_message)
                return None

            # Wait for scraping status "done"
            while True:

                sleep(15)

                # Get scraping status
                scraping_status = api.get_status()

                # Detect errors
                if not scraping_status:
                    self.send_message(chat_id, error_message)
                    return None

                # End loop
                if scraping_status == "done":
                    break

            # Get preview url
            preview_url = api.get_preview()
            preview_message += preview_url
            self.send_message(chat_id, preview_message)
