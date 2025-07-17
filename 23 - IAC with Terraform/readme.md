# Infrastructure as Code (IaC) with Terraform

This use case focuses on provisioning AWS infrastructure using Terraform, an open-source Infrastructure as Code tool. It eliminates the need for manual resource creation and ensures reproducible and version-controlled infrastructure deployments.

## Objective

Automate the creation of AWS resources (VPC, EC2, S3, etc.) using Terraform scripts.

## What Was Done

- Installed and configured Terraform locally
- Created a Terraform configuration file (`.tf`) defining the infrastructure
- Used AWS provider for managing resources
- Applied the plan to provision resources in AWS

## Key Components

- **Terraform Provider**: AWS
- **Resources Created**:
  - VPC
  - EC2 Instance
  - S3 Bucket
- **Variables**: Used to parameterize the infrastructure for flexibility
- **State Management**: `.tfstate` file stores current infrastructure state

## Terraform Files

- `main.tf` – Main configuration file with resources
- `variables.tf` – Input variables for customization
- `outputs.tf` – Output values like EC2 IP address
- `terraform.tfvars` – Actual variable values used during deployment

## Commands Used

terraform init # Initialize working directory
terraform plan # Preview infrastructure changes
terraform apply # Apply and create resources
terraform destroy # Destroy all resources created


## Benefits

- Repeatable and consistent infrastructure deployment
- Easy rollback with version-controlled `.tf` files
- Scalable and modular setup using Terraform modules

## Notes

- Ensure proper IAM credentials are set in the environment
- Can be extended to include RDS, IAM roles, Lambda, etc.
