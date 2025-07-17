# Auto-Remediation Using CloudWatch + Lambda

This use case demonstrates how to automatically respond to AWS infrastructure issues using CloudWatch alarms and Lambda functions.

## Overview

Auto-remediation is a self-healing mechanism where Lambda functions are triggered in response to CloudWatch alarms to take corrective actions — like restarting an EC2 instance or cleaning up unused resources.

## Steps Implemented

1. **Create a CloudWatch Alarm**
   - Set up a CloudWatch alarm to monitor EC2 instance status checks.
   - Trigger an action when a threshold is breached (e.g., failed status checks).

2. **Lambda Function for Remediation**
   - Wrote a Python Lambda function to perform remediation (e.g., stop and start EC2 instance).
   - Attached appropriate IAM permissions to allow instance operations.

3. **Alarm Action Configuration**
   - Configured the alarm to invoke the Lambda function when it enters the `ALARM` state.

4. **Testing and Validation**
   - Simulated failure states and verified auto-remediation.

## Key Concepts

- **Event-driven Remediation**: Automatically resolve incidents based on monitoring events.
- **Operational Efficiency**: Minimizes manual intervention during failures.
- **Cloud-native Monitoring**: Uses AWS-native tools like CloudWatch and Lambda.

## AWS Services Used

- Amazon CloudWatch (for monitoring and triggering alarms)
- AWS Lambda (for executing remediation logic)
- EC2 (the target service being remediated)
- IAM (role with permissions for Lambda to manage EC2)

## Files Included

- `remediation_lambda.py` – Lambda function to remediate EC2 issues.
- `cloudwatch_alarm_setup.json` – CloudFormation or manual alarm configuration reference.
- `auto_remediation_documentation.pdf` – Documentation and explanation of flow.
