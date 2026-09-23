variable "app_name" {
  type    = string
  default = "orders-api"
}

variable "environment" {
  type    = string
  default = "dev"
}

variable "replica_count" {
  type    = number
  default = "three"
}

variable "enable_debug" {
  type    = bool
  default = "yes"
}
