# Serverless Image Processing

This use case demonstrates how to build a fully serverless image processing workflow using AWS Lambda and S3. When an image is uploaded to a source S3 bucket, a Lambda function is triggered to resize or process the image and store the output in a destination S3 bucket.

## Overview

A serverless architecture is used to automate image transformations without managing any servers. The architecture ensures scalability, minimal cost, and real-time processing.

## Steps Implemented

1. **Create Two S3 Buckets**
   - Source bucket to upload original images
   - Destination bucket to store processed images

2. **Lambda Function for Image Processing**
   - Configured trigger from the source S3 bucket
   - Used Python PIL (Pillow) library to resize images
   - Processed image saved to destination bucket

3. **Set Up Lambda Layers**
   - Created a layer for PIL (Pillow) dependencies
   - Attached the layer to the Lambda function for modular deployment

4. **Permissions**
   - Attached IAM role to Lambda with permissions for both S3 buckets
   - Configured S3 bucket trigger policies

5. **Testing**
   - Uploaded sample `.jpg` and `.png` images
   - Verified processed images in the destination bucket

## Key Concepts

- Event-driven processing using S3 + Lambda
- Image transformation with Pillow
- Using Lambda layers for third-party libraries
- Role-based access control for S3 operations

## AWS Services Used

- AWS Lambda
- Amazon S3
- AWS IAM
- Lambda Layers
- AWS CloudWatch (for logging)

## Files Included

- `lambda_function.py` – Python code for image processing
- `layer_requirements.txt` – Dependencies for the layer
- `serverless_image_processing_documentation.pdf` – Step-by-step setup documentation
