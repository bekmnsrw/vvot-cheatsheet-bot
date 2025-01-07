from os import getenv

# Telegram

TELEGRAM_BOT_API_HOST = "https://api.telegram.org"
TG_BOT_KEY = getenv("TG_BOT_KEY")

TELEGRAM_API_URL = f"{TELEGRAM_BOT_API_HOST}/bot{TG_BOT_KEY}"
TELEGRAM_IMAGE_URL = f"{TELEGRAM_BOT_API_HOST}/file/bot{TG_BOT_KEY}"

# Yandex Cloud

YC_API_OCR_URL = "https://ocr.api.cloud.yandex.net/ocr/v1/recognizeText"
YC_API_GPT_URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

FOLDER_ID = getenv("FOLDER_ID")
BUCKET_NAME = getenv("BUCKET_NAME")
BUCKET_GPT_INSTRUCTION_KEY = getenv("BUCKET_GPT_INSTRUCTION_KEY")
