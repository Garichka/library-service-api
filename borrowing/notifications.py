import requests
from django.conf import settings


def send_telegram_notification(message):
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {"chat_id": chat_id, "text": message, "parse_mode": "HTML"}

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending telegram notification: {e}")
