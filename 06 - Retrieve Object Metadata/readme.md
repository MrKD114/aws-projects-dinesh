# Retrieving Object Metadata from Amazon S3 using Boto3

This use case demonstrates how to programmatically retrieve metadata of objects stored in an S3 bucket using Python and Boto3.

## Overview

The script fetches metadata such as content type, size, last modified date, and storage class of a specific object in an S3 bucket. This is useful for analyzing object properties without downloading the file.

## Steps Implemented

1. **Environment Setup**
   - Installed Python and the `boto3` package.
   - Configured AWS credentials using:
     ```
     aws configure
     ```

2. **Retrieve Object Metadata Script**
   - Script connects to S3, accesses a specific bucket, and retrieves metadata for a given object key.
   - Sample code:
     ```python
     import boto3

     s3 = boto3.client('s3')
     response = s3.head_object(Bucket='your-bucket-name', Key='your-object-key')

     print("Metadata:")
     print(f" - Content Type: {response['ContentType']}")
     print(f" - Size: {response['ContentLength']} bytes")
     print(f" - Last Modified: {response['LastModified']}")
     print(f" - Storage Class: {response.get('StorageClass', 'STANDARD')}")
     ```

3. **Permissions Required**
   - IAM user/role should have `s3:HeadObject` and `s3:GetObject` permissions.

4. **Execution**
   - Replace the bucket name and object key with actual values before running the script.

## Key Concepts

- S3: Scalable object storage service from AWS.
- Object Metadata: Includes properties like file type, size, timestamps, etc.
- Boto3: AWS SDK for Python to interact with S3 and other services.

## Files Included

- `get_s3_metadata.py` – Script to retrieve object metadata
- `S3_Metadata_Documentation.pdf` – Documentation with setup instructions and usage notes
