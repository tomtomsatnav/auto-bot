terraform {
  required_version = ">= 1.5"

  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}

locals {
  config = {
    app      = var.app_name
    env      = var.enviroment
    replicas = var.replica_count
    debug    = var.enable_debug
  }
}

resource "local_file" "app_config" {
  filename = "${path.module}/output/${var.app_name}-${var.environment}.json"
  content  = jsonencode(local.config)
}

resource "local_file" "readme" {
  filename = "${path.module}/output/README.txt"
  content  = "Config generated at local_file.app_config.filename"
}
