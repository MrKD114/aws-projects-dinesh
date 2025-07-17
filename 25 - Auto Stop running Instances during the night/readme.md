# Auto Stop Running Instances During the Night

This use case automates the process of stopping running EC2 instances during non-business hours (e.g., night) to save costs.

## Objective

Automatically stop EC2 instances at a scheduled time (e.g., 8 PM daily) using AWS Lambda and EventBridge to avoid unnecessary billing.

## What Was Done

- Created an AWS Lambda function using Python (Boto3) that:
  - Lists all EC2 instances
  - Filters instances based on running state
  - Stops only running instances
- Created an EventBridge rule with a cron expression to trigger the Lambda function at 8 PM every day
- Assigned necessary IAM permissions to the Lambda function for EC2 actions

## Key Components

- **Lambda Function**: Python-based script to stop EC2 instances
- **EventBridge Rule**: Scheduled trigger (cron-based) for Lambda execution
- **IAM Role**: Permissions to describe and stop EC2 instances

## Cron Expression Used

cron(30 14 * * ? *)

> This expression runs the Lambda at 8:30 PM IST every day (14:30 UTC).

## Security Considerations

- IAM role is scoped only to necessary EC2 actions
- Logs written to CloudWatch for audit purposes

## Benefits

- Cost-saving by avoiding charges from idle EC2 instances overnight
- Fully automated with no manual intervention required
- Scalable across all regions (can extend to include filtering by tags or regions)

## Notes

- Can be modified to exclude production or critical instances using tags
- Extendable to start instances again in the morning using another rule
