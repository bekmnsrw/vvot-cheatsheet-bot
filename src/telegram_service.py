from requests import post, get
from settings import TELEGRAM_API_URL, TELEGRAM_IMAGE_URL
from constants import SUCCESS
from utils import encode_to_base64

def send_message(text, message):
    url = f"{TELEGRAM_API_URL}/sendMessage"

    json = {
        "chat_id": message["chat"]["id"],
        "text": text,
        "reply_parameters": { 
            "message_id": message["message_id"],
        },
    }

    post(url=url, json=json)

def get_image_by_id(id):
    url = f"{TELEGRAM_API_URL}/getFile"
    params = { 
        "file_id": id,
    }
    
    response = get(url=url, params=params)

    if response.status_code == SUCCESS:
        image_path = response.json()["result"].get("file_path")
        get_image_by_path(image_path)
    else:
        return None

def get_image_by_path(image_path):
    url = f"{TELEGRAM_IMAGE_URL}/{image_path}"

    response = get(url=url)

    if response.status_code == SUCCESS:
        image_bytes = response.content
        return encode_to_base64(image_bytes)
    else:
        return None
