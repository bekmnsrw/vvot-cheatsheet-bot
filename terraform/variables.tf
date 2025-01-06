variable "cloud_id" {
    type        = string
    description = "Идентификатор облака"
}

variable "folder_id" {
    type        = string
    description = "Идентификатор каталога"
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

variable "terraform_version" {
    type = string
    description = "Версия Terraform"
    default = ">= 0.13"
}

variable "yandex_zone" {
    type = string
    description = "Зоны доступности Yandex Cloud"
    default = "ru-central1-a"
}

variable "yandex_source" {
    type    = string
    default = "yandex-cloud/yandex"
}

variable "telegram_source" {
    type    = string
    default = "yi-jiayu/telegram"
}

variable "telegram_version" {
    type        = string
    description = "Версия Terraform Provider for Telegram"
    default     = "0.3.1"
}
