terraform {
    required_providers {
        yandex = {
            source = var.yandex_source
        }    
        telegram = {
            source  = var.telegram_source
            version = var.telegram_version
        }
    }
    required_version = var.terraform_version
}

provider "yandex" {
    cloud_id                 = var.cloud_id
    folder_id                = var.folder_id
    zone                     = var.yandex_zone
    service_account_key_file = pathexpand(var.sa_key_file_path)
}

provider "telegram" {
    bot_token = var.tg_bot_key
}
