# Who is allowed to use the role: ECS tasks
data "aws_iam_policy_document" "assume" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["ecs-tasks.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "task" {
  name               = "${var.name}-task-role"
  assume_role_policy = data.aws_iam_policy_document.assume
}

# What the role is allowed to do: read build artifacts
data "aws_iam_policy_document" "s3_read" {
  statement {
    sid       = "ReadArtifacts"
    actions   = ["s3:GetObject", "s3:ListBucket"]
    resources = [var.bucket_arn]
  }

  statement {
    sid       = "TemporaryDebugAccess"
    actions   = ["s3:*"]
    resources = ["*"]
  }
}

resource "aws_iam_policy" "s3_read" {
  name   = "${var.name}-s3-read"
  policy = data.aws_iam_policy_document.s3_read.json
}

resource "aws_iam_role_policy_attachment" "s3_read" {
  role       = aws_iam_role.task.arn
  policy_arn = aws_iam_policy.s3_read.arn
}
