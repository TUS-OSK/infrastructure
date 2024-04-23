terraform {
  backend "s3" {
    bucket         = "osk-terraform-state-growi"
    key            = "terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "osk-terraform-statelock-growi"
    encrypt        = true
  }
}
