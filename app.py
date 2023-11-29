import os
from flask import Flask, request
from dotenv import load_dotenv
from bot import Bot
from threading import Thread

# Read settings
load_dotenv()
PORT = int(os.environ.get('PORT', 5000))

# Start flask
app = Flask(__name__)
bot = Bot()


@app.get("/")
def index():
    return {
        "status": "success",
        "message": "service running",
        "data": []
    }


@app.post("/")
def webhook():
    """ Main webhook endpint with workflow
    """
    data = request.json

    # Get message parts
    message = data["message"]
    message_text = message["text"]
    message_chat_id = message["chat"]["id"]

    # Run main workflow
    workflow_thread = Thread(
        target=bot.workflow,
        args=(message_text, message_chat_id))
    workflow_thread.start()

    # Return success
    return {
        "status": "success",
        "message": "message sent",
        "data": []
    }


if __name__ == "__main__":
    app.run(port=PORT)
