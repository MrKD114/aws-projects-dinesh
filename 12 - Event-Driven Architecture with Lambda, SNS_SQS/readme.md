# Event-Driven Architecture with Lambda, SNS, and SQS

This use case demonstrates an event-driven serverless architecture where a file upload triggers a Lambda function, which publishes a message to an SNS topic. The SNS topic fans out the message to one or more SQS queues, which can be further processed asynchronously by another Lambda function.

## Overview

This architecture enables decoupling between services and reliable asynchronous communication using managed AWS services.

## Steps Implemented

1. **S3 Bucket Setup**
   - Created a bucket to upload test files.
   - Enabled event notifications for object creation.

2. **Lambda Function (L1)**
   - Triggered by the S3 bucket when a new file is uploaded.
   - Extracted metadata and published to SNS topic.

3. **SNS Topic**
   - Created a topic to handle messages published by Lambda L1.
   - Subscribed an SQS queue to this topic.

4. **SQS Queue**
   - Subscribed to the SNS topic.
   - Received messages from SNS.

5. **Lambda Function (L2)**
   - Triggered by new messages in SQS queue.
   - Processed the message and optionally sent an email or stored logs.

## Key Concepts

- **Event-Driven**: Architecture that responds to events like file uploads.
- **Decoupling**: Lambda and downstream consumers are not tightly coupled.
- **Asynchronous Flow**: Processing can be done independently and reliably.

## AWS Services Used

- S3 (file trigger)
- Lambda (event processors)
- SNS (fan-out messaging)
- SQS (durable message queue)

## Files Included

- `lambda_file_upload_trigger.py` – L1 function to send metadata to SNS
- `lambda_sqs_processor.py` – L2 function to consume and process SQS messages
- `event_architecture_documentation.pdf` – Diagrams and step-by-step explanation of the setup
