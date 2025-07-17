# Deploying a Simple Serverless App

This use case demonstrates how to deploy a basic serverless application using AWS Lambda, Amazon API Gateway, and IAM roles. It highlights the practical implementation of a fully managed, event-driven architecture without provisioning or managing servers.

## Overview

We are deploying a REST API endpoint that triggers an AWS Lambda function. The Lambda function simply returns a JSON response, simulating a backend API service.

## Steps Implemented

1. **Lambda Function Creation**
   - Created a Lambda function using Python runtime.
   - Example code:
     ```python
     def lambda_handler(event, context):
         return {
             'statusCode': 200,
             'body': 'Hello from Serverless App!'
         }
     ```
   - IAM role attached with `AWSLambdaBasicExecutionRole`.

2. **API Gateway Setup**
   - Created a REST API via API Gateway.
   - Defined a resource path `/hello` and method `GET`.
   - Integrated the method with the Lambda function.

3. **Enable CORS (Optional)**
   - Allowed necessary headers for cross-origin requests.

4. **Deploy API Gateway**
   - Created a new deployment stage (e.g., `dev`).
   - Copied the Invoke URL for testing.

5. **Test the Endpoint**
   - Called the URL using browser or Postman:
     ```
     https://<api-id>.execute-api.<region>.amazonaws.com/dev/hello
     ```
   - Response:
     ```
     Hello from Serverless App!
     ```

## Key Concepts

- AWS Lambda: Serverless compute engine.
- Amazon API Gateway: API hosting and request routing.
- IAM Roles: Lambda execution and API Gateway integration permissions.

## Files Included

- `lambda_function.py` – Lambda handler code
- `serverless_app_postman.json` – Sample Postman collection for testing
- `Serverless_App_Deployment_Documentation.pdf` – Detailed implementation guide

