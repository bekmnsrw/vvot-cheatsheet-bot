from os import getenv

# Telegram

TELEGRAM_BOT_API_HOST = "https://api.telegram.org"
TELEGRAM_BOT_TOKEN = getenv("TELEGRAM_BOT_TOKEN")

TELEGRAM_API_URL = f"{TELEGRAM_BOT_API_HOST}/bot{TELEGRAM_BOT_TOKEN}"
TELEGRAM_IMAGE_URL = f"{TELEGRAM_BOT_API_HOST}/file/bot{TELEGRAM_BOT_TOKEN}"

# Yandex Cloud

YC_API_OCR_URL = "https://ocr.api.cloud.yandex.net/ocr/v1/recognizeText"
YC_API_GPT_URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

FOLDER_ID = getenv("FOLDER_ID")
BUCKET_NAME = getenv("BUCKET_NAME")
BUCKET_GPT_INSTRUCTION_KEY = getenv("BUCKET_GPT_INSTRUCTION_KEY")
