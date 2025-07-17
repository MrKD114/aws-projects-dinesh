import boto3

ec2 = boto3.client('ec2', region_name = 'ap-south-1')
InstanceId = 'i-0997c6e8e7102f990'

try:
    ec2.terminate_instances(InstanceIds=[InstanceId])
    print(f"Successfully terminated instance {InstanceId}")
except Exception as e:
    print(e)