import boto3

Lambda = boto3.client('lambda', region_name = 'ap-south-1')

bucket = input("Please re-enter the bucket name : ")
FunctionName = "S3TriggeredLambda"

def GrantPermissionToInvoke():
    try:
        response = Lambda.add_permission(
            FunctionName = FunctionName,
            StatementId = 'AllowInvoke',
            Action = 'lambda:InvokeFunction',
            Principal = 's3.amazonaws.com',
            SourceArn = f'arn:aws:s3:::{bucket}'
        )
        print(f"Invoke Permission granted to S3 Bucket : {bucket}")
    except Exception as e:
        print(e)

GrantPermissionToInvoke()