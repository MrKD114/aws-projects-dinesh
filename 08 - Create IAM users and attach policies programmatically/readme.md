# Create IAM Users and Attach Policies using Python and Boto3

This use case demonstrates how to create IAM users and attach predefined policies programmatically using Python scripts with the Boto3 SDK.

## Overview

Creating IAM users and assigning permissions programmatically helps automate user onboarding and maintain consistent security policies across environments.

## Steps Implemented

1. **Environment Setup**
   - Installed Python and the `boto3` package.
   - Configured AWS credentials with admin-level access using:
     ```
     aws configure
     ```

2. **Script Functionalities**
   - Create a new IAM user.
   - Attach an AWS-managed policy like `AmazonS3ReadOnlyAccess` or custom policy.
   - Optionally create access keys for programmatic access.

   Example code snippet to create a user and attach a policy:
   ```python
   import boto3

   iam = boto3.client('iam')

   # Create a new IAM user
   response = iam.create_user(UserName='newuser')

   # Attach a policy to the user
   iam.attach_user_policy(
       UserName='newuser',
       PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'
   )

   print("Created IAM user and attached policy successfully.")
