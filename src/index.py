from json import loads
from constants import SUCCESS, START_COMMAND, HELP_COMMAND, START_MESSAGE, HELP_MESSAGE, GET_UNHANDLED_MESSAGE_TYPE_ERROR_MESSAGE, CANT_ANSWER_ERROR_MESSAGE, GET_INCORRECT_PHOTO_ERROR_MESSAGE
from telegram_service import send_message, get_image_by_id
from yandex_service import get_gpt_answer

def handler(event, context):
    update = loads(event["body"])
    message = update.get("message")

    if message:
        token = context.token["access_token"]
        handle_message(message, token)

    return { 
        "statusCode": SUCCESS,
    }

def handle_message(message, token):
    # Получаем текст сообщения, если он есть
    text = message.get("text")

    # Отправляем сообщение в ответ на команду /start
    if text == START_COMMAND:
        send_message(START_MESSAGE, message)

    # Отправляем сообщение в ответ на команду /help
    elif text == HELP_COMMAND:
        send_message(HELP_MESSAGE, message)

    # Если сообщение содержит обычный текст, обрабатываем его
    elif text is not None:
        handle_text_message(text, message, token)

    # Если сообщение содержит изображение, обрабатываем его
    elif image := message.get("photo"):
        handle_image_message(image, message, token)

    # В противном случае, если сообщение состоит не из текста или изображения, отправляем сообщение об ошибке
    else:
        send_message(GET_UNHANDLED_MESSAGE_TYPE_ERROR_MESSAGE, message)

def handle_text_message(text, message, token):
    gpt_answer = get_gpt_answer(question=text, token=token)

    if gpt_answer:
        send_message(gpt_answer, message)
    else:
        send_message(CANT_ANSWER_ERROR_MESSAGE, message)

def handle_image_message(image, message, token):
    image_id = image[-1]["file_id"]
    image = get_image_by_id(image_id)
    
    # TODO: Add YandexOCR answer
    recognized_text = "" 

    if recognized_text:
        handle_text_message(recognized_text, message, token)
    else:
        send_message(GET_INCORRECT_PHOTO_ERROR_MESSAGE, message)    