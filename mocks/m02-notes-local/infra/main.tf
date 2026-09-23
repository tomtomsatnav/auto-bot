terraform {
  required_version = ">= 1.5"

  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

# Talks to Docker Desktop on your Mac
provider "docker" {}

variable "external_port" {
  type    = number
  default = 8080
}

resource "docker_image" "notes" {
  name = "drills/notes-api:dev"

  build {
    context = "${path.module}/app"
  }
}

resource "docker_volume" "notes" {
  name = "notes-data"
}

resource "docker_container" "notes" {
  name  = "notes-api"
  image = docker_image.notes.image_id

  env = {
    NOTE_DIR = "/data/notes"
  }

  ports {
    internal = 8080
    external = var.external_port
  }

  volumes {
    volume_name    = docker_volume.notes.name
    container_path = "/data"
  }
}

output "health_url" {
  value = "http://localhost:${var.external_port}/health"
}
