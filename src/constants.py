# Telegram bot messages in response to commands: /start, /help

START_MESSAGE = """
Я помогу подготовить ответ на экзаменационный вопрос по дисциплине "Операционные системы".
Пришлите мне фотографию с вопросом или наберите его текстом.
"""

HELP_MESSAGE = """
Я помогу подготовить ответ на экзаменационный вопрос по дисциплине "Операционные системы".
Пришлите мне фотографию с вопросом или наберите его текстом.
"""

# Telegram bot messages in case of error

CANT_ANSWER_ERROR_MESSAGE = """
Я не смог подготовить ответ на экзаменационный вопрос.
"""

GET_MORE_THAN_ONE_PHOTO_ERROR_MESSAGE = """
Я могу обработать только одну фотографию.
"""

GET_INCORRECT_PHOTO_ERROR_MESSAGE = """
Я не могу обработать эту фотографию.
"""

GET_UNHANDLED_MESSAGE_TYPE_ERROR_MESSAGE = """
Я могу обработать только текстовое сообщение или фотографию.
"""

# Status codes

SUCCESS = 200
