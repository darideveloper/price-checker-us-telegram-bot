import os
import csv
import requests
from dotenv import load_dotenv
load_dotenv()

# Get settings
WEBHOOK = os.getenv('WEBHOOK')

# generate csv path
current_folder = os.path.dirname(__file__)
parent_folder = os.path.dirname(current_folder)
csv_path = os.path.join(parent_folder, 'bots_tokens.csv')

# read csv file
with open(csv_path, 'r') as csv_file:
    reader = list(csv.reader(csv_file))
    for row in reader[1:]:
        bot_name, bot_token = row

        print(f"setting webhook for {bot_name}...")

        # Generate set webhook bot url
        url = f"https://api.telegram.org/bot{bot_token}" \
            f"/setWebhook?url={WEBHOOK}"

        # Send request
        res = requests.get(url)
        res.raise_for_status()

        # Print response
        print(f"\tStatus code: {res.status_code}")
