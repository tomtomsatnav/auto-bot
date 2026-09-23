variable "region" {
  type    = string
  default = "eu-west-2"
}

variable "name" {
  type    = string
  default = "orders-api"
}

variable "bucket_arn" {
  type        = string
  description = "ARN of the artifacts bucket the service reads from"
  default     = "arn:aws:s3:::platform-drills-dev-artifacts"
}
