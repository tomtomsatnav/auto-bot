output "ecr_repository_url" {
  value = aws_ecr_repository.app.repository_url
}

output "service_name" {
  value = aws_ecs_service.app.name
}
