# Cloud Resource Cleanup

This use case implements a Python script using Boto3 to automate the cleanup of unused or temporary AWS resources across services. It helps in reducing unnecessary costs and maintaining a tidy cloud environment.

## Overview

The goal is to identify and delete stale or test resources such as:
- EC2 instances
- Unattached EBS volumes
- Unused Elastic IPs
- S3 buckets with test data
- Lambda functions used for experiments
- CloudWatch log groups
- Orphaned security groups

## Steps Implemented

1. **Setup**
   - Configured Boto3 and AWS credentials.
   - Required IAM permissions: `ec2:Describe*`, `ec2:Delete*`, `s3:List*`, `s3:Delete*`, `lambda:DeleteFunction`, etc.

2. **Script Functionality**
   - Listed EC2 instances with specific tags or stopped status and deleted them.
   - Identified and deleted unattached EBS volumes.
   - Released unused Elastic IPs.
   - Listed and removed S3 buckets with prefix `test-` or empty content.
   - Deleted Lambda functions tagged as temporary or with test naming.
   - Cleaned up unused CloudWatch log groups older than a specified retention period.
   - Identified and removed orphaned security groups (not attached to any ENI).

3. **Safety Measures**
   - Added filters to ensure only test/stale resources are deleted.
   - Added dry-run option for verification before actual deletion.

## Key Concepts

- AWS resource tagging
- Automation of cleanup tasks
- Cost optimization by removing idle resources

## AWS Services Used

- Amazon EC2
- Amazon S3
- AWS Lambda
- Amazon CloudWatch
- AWS Boto3 SDK

## Files Included

- `cleanup_resources.py` – Python script to perform resource cleanup.
- `cleanup_report.csv` – Optional report of deleted resources.
- `cloud_cleanup_documentation.pdf` – Documentation describing the cleanup flow and supported services.
