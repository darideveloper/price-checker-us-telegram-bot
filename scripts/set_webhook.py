import os
import requests
from dotenv import load_dotenv
load_dotenv()

# Get settings
WEBHOOK = os.getenv('WEBHOOK')
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Generate set webhook bot url
url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={WEBHOOK}"

# Send request
res = requests.get(url)
res.raise_for_status()
print(res.json())
