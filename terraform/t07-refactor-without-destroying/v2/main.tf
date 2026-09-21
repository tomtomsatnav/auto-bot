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

resource "random_pet" "name" {
  length = 2
}

locals {
  services = toset(["api", "worker"])
}

resource "local_file" "service" {
  for_each = local.services

  filename = "${path.module}/output/${each.key}.txt"
  content  = "${each.key} on ${random_pet.name.id}"
}
