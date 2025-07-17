# Serverless Feedback Application

This use case implements a simple feedback collection system using AWS serverless services. Users submit feedback via a frontend interface, which gets processed and stored using Lambda and DynamoDB without any server management.

## Overview

The application allows users to submit feedback (name, email, comments), which is processed by a backend Lambda function and stored in DynamoDB.

## Steps Implemented

1. **Frontend**
   - A basic HTML form to collect user feedback (name, email, message).
   - Form submits feedback via HTTP POST to an API Gateway endpoint.

2. **API Gateway**
   - REST API created with a single POST method.
   - Integrated with a Lambda function backend.

3. **Lambda Function**
   - Triggered by API Gateway to handle incoming POST requests.
   - Parses input, validates it, and writes the feedback data into DynamoDB.

4. **DynamoDB Table**
   - Stores each feedback entry with timestamp as the primary key.

5. **CORS Configuration**
   - Enabled on API Gateway to allow frontend-hosted domains.

6. **Security**
   - IAM role for Lambda with `dynamodb:PutItem` permissions.
   - Input validation to prevent malformed submissions.

## Key Concepts

- Serverless web applications
- REST API integration with Lambda
- Data persistence using DynamoDB
- End-to-end serverless workflow

## AWS Services Used

- Amazon API Gateway
- AWS Lambda
- Amazon DynamoDB
- AWS IAM

## Files Included

- `feedback_form.html` – Frontend form.
- `lambda_feedback_handler.py` – Lambda function to handle and store feedback.
- `feedback_schema.png` – Diagram of DynamoDB table structure.
- `serverless_feedback_app_documentation.pdf` – Documentation with architecture, flow, and configurations.
