terraform {
  required_version = ">= 1.5"

  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}

module "api_config" {
  source = "./module/service-config"

  service_name = "orders-api"
  port         = 8000
}

module "worker_config" {
  source = "./modules/service-config"

  service_name = "orders-worker"
}

output "api_config_path" {
  value = module.api_config.file_path
}

output "worker_config_path" {
  value = module.worker_config.config_path
}
