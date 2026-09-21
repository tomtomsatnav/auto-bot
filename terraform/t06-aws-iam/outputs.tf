output "task_role_arn" {
  value = aws_iam_role.task.arn
}

output "s3_read_policy_json" {
  value = data.aws_iam_policy_document.s3_read.json
}
