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

resource "random_pet" "server_name" {
  length = 2
}

resource "local_file" "api" {
  filename = "${path.module}/output/api.txt"
  content  = "api on ${random_pet.server_name.id}"
}

resource "local_file" "worker" {
  filename = "${path.module}/output/worker.txt"
  content  = "worker on ${random_pet.server_name.id}"
}
