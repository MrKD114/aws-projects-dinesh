import boto3

Ec2 = boto3.client('ec2', region_name='ap-south-1')

InstanceId = 'i-0997c6e8e7102f990'
try:
    Ec2.reboot_instances(InstanceIds=[InstanceId])
    print(f"Reboot successful for the instance {InstanceId}")
except Exception as e:
    print(e)