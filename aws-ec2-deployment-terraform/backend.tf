terraform {
  backend "s3" {
    bucket = "jenkins-terraform-aws"
    key    = "backend/terraform.tfstate"
    region = "eu-west-2"
  }
}