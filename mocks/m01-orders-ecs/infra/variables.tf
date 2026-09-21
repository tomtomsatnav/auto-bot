variable "region" {
  type    = string
  default = "eu-west-2"
}

variable "name" {
  type    = string
  default = "orders-api"
}

variable "vpc_id" {
  type    = string
  default = "vpc-0123456789abcdef0"
}

variable "vpc_cidr" {
  type    = string
  default = "10.0.0.0/16"
}

variable "subnet_ids" {
  type    = list(string)
  default = ["subnet-0aaaaaaaaaaaaaaaa", "subnet-0bbbbbbbbbbbbbbbb"]
}

variable "execution_role_arn" {
  type    = string
  default = "arn:aws:iam::123456789012:role/ecsTaskExecutionRole"
}

variable "desired_count" {
  type    = number
  default = 2
}
