# Send Alerts via SNS and Set Up CloudWatch Alarms Using Python

This use case automates the process of configuring CloudWatch alarms and sending notifications through SNS using Python scripts with Boto3.

## Overview

CloudWatch Alarms help monitor AWS resources and applications in real-time. SNS (Simple Notification Service) sends alerts via email, SMS, or HTTP endpoints when alarms are triggered.

## Steps Implemented

1. **Set Up SNS Topic and Subscription**
   - Created a new SNS topic.
   - Subscribed an email address to receive notifications.
   - Confirmed the email subscription.

   Example:
   ```python
   sns = boto3.client('sns')
   response = sns.create_topic(Name='EC2_Alarm_Topic')
   topic_arn = response['TopicArn']

   sns.subscribe(
       TopicArn=topic_arn,
       Protocol='email',
       Endpoint='your-email@example.com'
   )
