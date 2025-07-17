# Cleanup Script to Delete Testing Resources

This use case focuses on automating the cleanup of temporary AWS resources created during testing and learning exercises. This helps avoid unnecessary costs and maintains a clean AWS environment.

## Overview

The script deletes selected AWS resources such as:

- EC2 instances
- S3 buckets
- IAM users
- Lambda functions
- SNS topics
- CloudWatch alarms

## Steps Implemented

1. **Identify Resources to Delete**
   - Collected resource names or IDs created for testing purposes.
   - Ensured only temporary/testing resources were targeted to avoid accidental deletion.

2. **Delete EC2 Instances**
   ```python
   ec2 = boto3.client('ec2')
   ec2.terminate_instances(InstanceIds=['i-0abcd1234efgh5678'])
