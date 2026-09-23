terraform {
  required_version = ">= 1.5"

  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.6"
    }
  }
}

variable "services" {
  type    = list(string)
  default = ["auth", "payments", "notifications"]
}

resource "random_password" "db" {
  for_each = var.services

  length  = 24
  special = false
}

resource "local_file" "env" {
  count = length(var.services)

  filename        = "${path.module}/output/${var.services[count.index]}.env"
  content         = "DB_PASSWORD=${random_password.db[count.index].result}\n"
  file_permission = "0600"
}

output "service_files" {
  value = local_file.env.filename
}
