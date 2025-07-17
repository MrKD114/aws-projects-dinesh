# Launch and Manage EC2 Instances using Python and Boto3

This use case demonstrates how to launch and manage EC2 instances using Python scripts with the Boto3 SDK.

## Overview

Automating EC2 instance creation helps streamline infrastructure provisioning, especially in DevOps and cloud automation scenarios. This script covers launching, listing, stopping, and terminating EC2 instances programmatically.

## Steps Implemented

1. **Environment Setup**
   - Installed Python and the `boto3` package.
   - Configured AWS credentials using:
     ```
     aws configure
     ```

2. **Script Functionalities**
   - Launch a new EC2 instance with a specific AMI, instance type, key pair, and security group.
   - Fetch and list existing EC2 instances.
   - Stop and terminate instances programmatically.

   Example code snippet to launch an EC2 instance:
   ```python
   import boto3

   ec2 = boto3.resource('ec2')

   instance = ec2.create_instances(
       ImageId='ami-0abcdef1234567890',  # Replace with a valid AMI ID
       MinCount=1,
       MaxCount=1,
       InstanceType='t2.micro',
       KeyName='your-key-pair',         # Replace with your key pair name
       SecurityGroups=['your-security-group']  # Replace with your security group
   )[0]

   print("Launched EC2 Instance with ID:", instance.id)
