import boto3

ec2 = boto3.resource('ec2', region_name='ap-south-1')

instances = ec2.create_instances(
    ImageId='ami-0b09627181c8d5778',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='MumbaiRegion', 
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'EC2InstanceFromPython'}]
        }
    ]
)

print(f"Launched instance with ID: {instances[0].id}")
