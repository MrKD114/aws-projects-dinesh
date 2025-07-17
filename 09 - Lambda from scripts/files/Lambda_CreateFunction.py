import boto3

lambda_client = boto3.client('lambda', region_name='ap-south-1')

with open("lambda_function.zip", "rb") as f:
    zipped_code = f.read()

response = lambda_client.create_function(
    FunctionName='S3TriggeredLambda',
    Runtime='python3.12',
    Role='arn:aws:iam::770424767712:role/LambdaExecRoleForS3',
    Handler='lambda_function.lambda_handler',
    Code={'ZipFile': zipped_code},
    Timeout=25,
    MemorySize=128,
    Publish=True
)

print(" Lambda created successfully.")
print(" Lambda ARN:", response['FunctionArn'])