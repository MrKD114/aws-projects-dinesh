import boto3

S3 = boto3.client('s3', region_name = 'ap-south-1')

def S3_CreateBucket(BucketName):
    try:
        S3.create_bucket(
            Bucket = BucketName,
            CreateBucketConfiguration={
                'LocationConstraint' : 'ap-south-1'
            }
        )
        print(f"Bucket created : {BucketName}")

    except Exception as e:
        print(e)

BucketName = input("Please enter your Bucket Name : ")
S3_CreateBucket(BucketName=BucketName)