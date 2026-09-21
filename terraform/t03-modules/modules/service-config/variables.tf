variable "service_name" {
  type        = string
  description = "Name of the service"
}

variable "port" {
  type        = number
  description = "Port the service listens on"
}

variable "environment" {
  type    = string
  default = "dev"
}
