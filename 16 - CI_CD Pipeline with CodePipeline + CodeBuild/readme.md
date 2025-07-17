# CI/CD Pipeline using AWS CodePipeline and CodeBuild

This use case sets up a continuous integration and continuous deployment (CI/CD) pipeline that automates code builds, tests, and deployments using AWS services like CodePipeline and CodeBuild.

## Overview

The goal is to streamline application delivery by integrating version control, build automation, and deployment into a single automated pipeline.

## Steps Implemented

1. **Source Stage Configuration**
   - Integrated GitHub repository as the source provider.
   - Configured webhooks or polling for automatic triggers on code commits.

2. **Build Stage with CodeBuild**
   - Created a `buildspec.yml` file to define the build process (e.g., install dependencies, run tests, build artifacts).
   - Provisioned a CodeBuild project with IAM roles and permissions.
   - Configured build environment (runtime, compute, timeout, etc.).

3. **Deploy Stage (optional)**
   - Deployed artifacts to:
     - S3 bucket (for static websites).
     - Lambda function (serverless app deployment).
     - EC2 instance (via scripts or CodeDeploy).

4. **Pipeline Configuration**
   - Used AWS CodePipeline to orchestrate the full CI/CD flow.
   - Defined pipeline stages: Source → Build → Deploy.

5. **Notifications**
   - Configured SNS for pipeline state change alerts (optional).

## Key Concepts

- **Continuous Integration (CI)**: Automatically build and test code on commit.
- **Continuous Deployment (CD)**: Automatically deploy after successful build.
- **Infrastructure as Code**: All pipeline resources can be managed using CloudFormation or Terraform.

## AWS Services Used

- AWS CodePipeline
- AWS CodeBuild
- AWS S3 / Lambda / EC2 / CodeDeploy (as deployment targets)
- AWS IAM (for pipeline roles)
- Amazon SNS (for optional notifications)

## Files Included

- `buildspec.yml` – Defines the CodeBuild build steps.
- `pipeline_config.json` – JSON configuration of pipeline structure.
- `ci_cd_pipeline_documentation.pdf` – End-to-end documentation of the CI/CD flow.
