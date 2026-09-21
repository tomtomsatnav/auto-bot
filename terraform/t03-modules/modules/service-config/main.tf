resource "local_file" "config" {
  filename = "${path.module}/output/${var.service_name}.json"

  content = jsonencode({
    service     = var.service_name
    port        = var.port
    environment = var.environment
  })
}
