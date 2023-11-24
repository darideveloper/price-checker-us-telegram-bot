import os
import json
import requests
from dotenv import load_dotenv
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

    def workflow(self, message: str, chat_id: int):
        """ Main bot workflow (get and send message)

        Args:
            message (str): message send by user
            chat_id (int): id of the chat with user
        """

        welcome_message = "hello"
        start_search_message = "estamos buscando"

        if message == "/start":
            self.send_message(chat_id, welcome_message)
        else:
            self.send_message(chat_id, start_search_message)
