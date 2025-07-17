# Deploy AWS Lambda Function Using Python and Boto3

This use case demonstrates how to create and deploy an AWS Lambda function programmatically using Python scripts and Boto3 SDK.

## Overview

Automating Lambda deployments using scripts is useful for CI/CD pipelines, repetitive infrastructure tasks, or environment setup.

## Steps Implemented

1. **Prepare the Environment**
   - Installed Python and the `boto3` library.
   - AWS credentials configured using:
     ```
     aws configure
     ```
   - Created a basic Lambda handler in a `lambda_function.py` file and zipped it:
     ```
     zip function.zip lambda_function.py
     ```

2. **Python Script Functionalities**
   - Creates an IAM role with `AWSLambdaBasicExecutionRole`.
   - Uploads the Lambda zip file to AWS.
   - Creates a Lambda function using the uploaded code.
   - Optionally sets up permissions or test event input.

   Example code snippet:
   ```python
   import boto3

   lambda_client = boto3.client('lambda')

   with open('function.zip', 'rb') as f:
       zipped_code = f.read()

   response = lambda_client.create_function(
       FunctionName='MyLambdaFunction',
       Runtime='python3.9',
       Role='arn:aws:iam::123456789012:role/MyLambdaExecutionRole',
       Handler='lambda_function.lambda_handler',
       Code=dict(ZipFile=zipped_code),
       Timeout=15,
       Publish=True
   )

   print("Lambda function created successfully.")
