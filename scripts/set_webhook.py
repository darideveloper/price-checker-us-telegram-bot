import os
import sys
import requests
from time import sleep
from dotenv import load_dotenv

# Add folder to path and import db
current_folder = os.path.dirname(__file__)
parent_folder = os.path.dirname(current_folder)
sys.path.append(parent_folder)
from database.db import DB

# Get settings
load_dotenv()
WEBHOOK = os.getenv('WEBHOOK')

# Instance of database
database = DB()
bots_data = database.get_bots()

# Update webhook for each bot
for bot in bots_data:

    bot_name = bot["name"]
    bot_token = bot["token"]

    print(f"setting webhook for {bot_name}...")

    # Generate set webhook bot url
    dynamic_webhook = f"{WEBHOOK}/{bot_name}"
    url = f"https://api.telegram.org/bot{bot_token}" \
        f"/setWebhook?url={dynamic_webhook}"

    # Send request
    res = requests.get(url)
    res.raise_for_status()

    # Print response
    print(f"\tStatus code: {res.status_code}")
    
    sleep(5)
