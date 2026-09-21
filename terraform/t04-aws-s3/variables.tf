variable "region" {
  type    = string
  default = "eu-west-2"
}

variable "project" {
  type        = string
  description = "Project name, used in resource names"
  default     = "Platform_Drills"
}

variable "environment" {
  type    = string
  default = "dev"
}
