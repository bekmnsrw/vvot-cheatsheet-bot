variable "cloud_id" {
    type        = string
    description = "Идентификатор облака в Yandex Cloud"
}

variable "folder_id" {
    type        = string
    description = "Идентификатор каталога в Yandex Cloud"
}

variable "tg_bot_key" {
    type        = string
    description = "Токен Telegram бота"
}

variable "bucket_name" {
    type        = string
    description = "Название бакета, в котором хранится объект с инструкцией к YandexGPT"
    default     = "cheatsheet-bot-bucket"    
}

variable "bucket_gpt_instruction_key" {
    type        = string
    description = "Ключ объекта в бакете, в котором написана инструкция к YandexGPT"
    default     = "gpt_instruction.txt"
}

variable "sa_key_file_path" {
    type        = string
    description = "Путь к авторизованному ключу сервисного аккаунта"
    default     = "~/.yc-keys/key.json"
}

variable "yandex_zone" {
    type = string
    description = "Зона доступности Yandex Cloud"
    default = "ru-central1-a"
}
