# Automating EC2 Instance Start/Stop using Python and Boto3

This use case demonstrates how to set up a Python environment with Boto3 and automate the process of starting and stopping Amazon EC2 instances using scripts.

## Overview

The scripts allow users to manage EC2 instances programmatically without using the AWS Console. This is useful for cost optimization, scheduled operations, or bulk instance management.

## Steps Implemented

1. **Environment Setup**
   - Installed Python (>= 3.6) and `boto3` library.
   - Configured AWS credentials using:
     ```
     aws configure
     ```

2. **Start EC2 Instance Script**
   - Script to start one or multiple instances using their Instance IDs.
   - Sample code:
     ```python
     import boto3
     ec2 = boto3.client('ec2')
     ec2.start_instances(InstanceIds=['i-0abc1234def567890'])
     ```

3. **Stop EC2 Instance Script**
   - Script to stop one or multiple instances.
   - Sample code:
     ```python
     import boto3
     ec2 = boto3.client('ec2')
     ec2.stop_instances(InstanceIds=['i-0abc1234def567890'])
     ```

4. **Permission Setup**
   - IAM user/role must have `ec2:StartInstances` and `ec2:StopInstances` permissions.

5. **Execution**
   - Scripts executed from local terminal or scheduled using cron/Windows Task Scheduler for automation.

## Key Concepts

- Boto3: AWS SDK for Python to interact with AWS services.
- EC2: Virtual server instances in the cloud.
- IAM Policies: Permission control for accessing AWS services through scripts.

## Files Included

- `start_ec2.py` – Script to start EC2 instances
- `stop_ec2.py` – Script to stop EC2 instances
- `EC2_Python_Boto3_Documentation.pdf` – Complete guide with prerequisites and execution steps
