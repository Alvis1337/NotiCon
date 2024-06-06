import requests
from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


class TelegramMessage:
    @staticmethod
    def send_telegram_message(message):
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            'chat_id': CHAT_ID,
            'text': message
        }
        requests.post(url, data=payload)
