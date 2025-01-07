from json import loads
from constants import SUCCESS
from constants import START_COMMAND, HELP_COMMAND
from constants import START_MESSAGE, HELP_MESSAGE
from constants import GET_UNHANDLED_MESSAGE_TYPE_ERROR_MESSAGE, CANT_ANSWER_ERROR_MESSAGE, GET_INCORRECT_PHOTO_ERROR_MESSAGE
from telegram_service import send_message, get_image_by_id
from yandex_service import get_gpt_answer, get_recognized_text

def handler(event, context):
    update = loads(event["body"])
    message = update.get("message")

    if message:
        token = context.token["access_token"]
        handle_message(message=message, token=token)

    return { 
        "statusCode": SUCCESS,
    }

def handle_message(message, token):
    # Получаем текст сообщения, если он есть
    text = message.get("text")

    # Отправляем сообщение в ответ на команду /start
    if text == START_COMMAND:
        send_message(text=START_MESSAGE, message=message)

    # Отправляем сообщение в ответ на команду /help
    elif text == HELP_COMMAND:
        send_message(text=HELP_MESSAGE, message=message)

    # Если сообщение содержит обычный текст, обрабатываем его
    elif text is not None:
        handle_text_message(text=text, message=message, token=token)

    # Если сообщение содержит изображение, обрабатываем его
    elif image := message.get("photo"):
        handle_image_message(image=image, message=message, token=token)

    # В противном случае, если сообщение состоит не из текста или изображения, отправляем сообщение об ошибке
    else:
        send_message(text=GET_UNHANDLED_MESSAGE_TYPE_ERROR_MESSAGE, message=message)

def handle_text_message(text, message, token):
    gpt_answer = get_gpt_answer(question=text, token=token)

    if gpt_answer:
        send_message(text=gpt_answer, message=message)
    else:
        send_message(text=CANT_ANSWER_ERROR_MESSAGE, message=message)

def handle_image_message(image, message, token):
    image_id = image[-1]["file_id"]
    base64_image = get_image_by_id(image_id)
    
    recognized_text = get_recognized_text(base64_image=base64_image, token=token) 

    if recognized_text:
        handle_text_message(text=recognized_text, message=message, token=token)
    else:
        send_message(text=GET_INCORRECT_PHOTO_ERROR_MESSAGE, message=message)    