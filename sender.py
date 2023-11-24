import json
import requests


def send_message(chat_id: int, text: str, bot_token: str):
    """ Send message to specified chat

    Args:
        chat_id (int): id of the chat with user
        text (str): text of the message
        bot_token (str): token of the bot
    """

    print(f"Sending message to {chat_id}: {text}")

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
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
