from pathlib import Path
from requests import post
from settings import FOLDER_ID, BUCKET_GPT_INSTRUCTION_KEY, BUCKET_NAME
from settings import YC_API_GPT_URL, YC_API_OCR_URL
from constants import SUCCESS

def get_gpt_answer(question, token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    with open(Path("/function/storage", BUCKET_NAME, BUCKET_GPT_INSTRUCTION_KEY), "r") as file:
        instruction = file.read()
    
    json = {
        "modelUri": f"gpt://{FOLDER_ID}/yandexgpt",
        "messages": [
            {
                "role": "system",
                "text": instruction,
            },
            {
                "role": "user",
                "text": question,
            },
        ],
    }

    response = post(url=YC_API_GPT_URL, headers=headers, json=json)

    if response.status_code != SUCCESS:
        return None
    
    alternatives = response.json()["result"]["alternatives"]

    final_alternatives = [
        alternative for alternative in alternatives
        if alternative["status"] == "ALTERNATIVE_STATUS_FINAL"
    ]

    if final_alternatives.count == 0:
        return None
    
    return final_alternatives[0]["message"].get("text")

def get_recognized_text(base64_image, token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    json = {
        "mimeType": "image/jpeg",
        "languageCodes": ["ru", "en"],
        "content": base64_image,
    }

    response = post(url=YC_API_OCR_URL, headers=headers, json=json)

    if response.status_code != SUCCESS:
        return None
    
    recognized_text = response.json()["result"]["textAnnotation"]["fullText"]

    if recognized_text:
        return recognized_text
    else:
        return None
