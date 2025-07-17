# Infrastructure as Code (IaC) with Python + CloudFormation

This use case demonstrates how to automate the provisioning of AWS infrastructure using CloudFormation templates triggered and managed by Python scripts.

## Overview

The goal is to treat infrastructure as version-controlled, repeatable code using AWS CloudFormation. Python (with Boto3) is used to deploy and manage the stacks programmatically.

## Steps Implemented

1. **Create a CloudFormation Template**
   - Defined resources like VPC, Subnets, EC2 Instances, S3 Buckets.
   - Written in YAML or JSON format.

2. **Python Script for Stack Deployment**
   - Used Boto3 to create or update a CloudFormation stack.
   - Handled stack status checks and error handling.

3. **Validation and Deletion**
   - Added logic to validate templates before deployment.
   - Script also supports stack deletion.

## Key Concepts

- **Infrastructure as Code (IaC)**: Treating infrastructure the same way as software — reproducible, consistent, and version-controlled.
- **Automation**: No manual creation of AWS resources via console.
- **Idempotency**: Scripts ensure repeated runs do not break existing resources.

## AWS Services Used

- CloudFormation (template-driven infrastructure creation)
- Boto3 (Python SDK for AWS API interaction)
- IAM (permissions for deploying stacks)

## Files Included

- `cloudformation_template.yaml` – Contains AWS infrastructure definitions.
- `deploy_stack.py` – Python script to deploy/update CloudFormation stack.
- `delete_stack.py` – Script to delete the CloudFormation stack.
- `iac_cloudformation_documentation.pdf` – Documentation and architecture explanation.
