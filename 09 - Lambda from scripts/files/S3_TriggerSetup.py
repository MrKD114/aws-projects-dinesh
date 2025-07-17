import boto3

Lambda = boto3.client('lambda', region_name='ap-south-1')

lambda_function_name = 'S3TriggeredLambda'
bucket  = input("Please re-enter your bucket name : ")

Lambda.add_permission(
    FunctionName=lambda_function_name, 
    StatementId='AllowS3Invoke',
    Action='lambda:InvokeFunction',
    Principal='s3.amazonaws.com',
    SourceArn=f'arn:aws:s3:::{bucket}'
)

print(" Permission granted.")
