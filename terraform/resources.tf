data "archive_file" "vvot_task1" {
    type        = "zip"
    source_dir  = "../src"
    output_path = "../build/content.zip"
}

resource "yandex_function" "cheatsheet_bot" {
    name               = "cheatsheet-bot"
    description        = "Функция, обрабатывающая сообщения, отправляемые Telegram боту"
    entrypoint         = "index.handler"
    runtime            = "python312"
    user_hash          = data.archive_file.vvot_task1.output_sha256
    memory             = 128
    service_account_id = yandex_iam_service_account.sa_cheatsheet_bot.id
    environment = {
        TELEGRAM_BOT_TOKEN          = var.tg_bot_key
        FOLDER_ID                   = var.folder_id
        BUCKET_NAME                 = var.bucket_name
        BUCKET_GPT_INSTRUCTION_KEY  = var.bucket_gpt_instruction_key
    }
    content {
        zip_filename = data.archive_file.vvot_task1.output_path
    }
    mounts {
        name = var.bucket_name
        mode = "ro"
        object_storage {
            bucket = yandex_storage_bucket.bucket_cheatsheet_bot.bucket
        }
    }
}

resource "telegram_bot_webhook" "webhook_cheatsheet_bot" {
    url = "https://functions.yandexcloud.net/${yandex_function.cheatsheet_bot.id}"
}

resource "yandex_iam_service_account" "sa_cheatsheet_bot" {
    name = "sa-cheatsheet-bot"
}

resource "yandex_storage_bucket" "bucket_cheatsheet_bot" {
    bucket = var.bucket_name
}

resource "yandex_storage_object" "yandex_gpt_instruction" {
    bucket = yandex_storage_bucket.bucket_cheatsheet_bot.id
    key    = var.bucket_gpt_instruction_key
    source = "gpt_instruction.txt"
}

resource "yandex_function_iam_binding" "iam_cheatsheet_bot" {
    function_id = yandex_function.cheatsheet_bot.id
    role        = "functions.functionInvoker"
    members     = [ "system:allUsers" ]
}

resource "yandex_resourcemanager_folder_iam_member" "ai_vision_cheatsheet_bot" {
    folder_id = var.folder_id
    role      = "ai.vision.user"
    member    = "serviceAccount:${yandex_iam_service_account.sa_cheatsheet_bot.id}"
}

resource "yandex_resourcemanager_folder_iam_member" "ai_language_models_cheatsheet_bot" {
    folder_id = var.folder_id
    role      = "ai.languageModels.user"
    member    = "serviceAccount:${yandex_iam_service_account.sa_cheatsheet_bot.id}"
}

resource "yandex_resourcemanager_folder_iam_member" "storage_viewer_cheatsheet_bot" {
    folder_id = var.folder_id
    role      = "storage.viewer"
    member    = "serviceAccount:${yandex_iam_service_account.sa_cheatsheet_bot.id}"
}
