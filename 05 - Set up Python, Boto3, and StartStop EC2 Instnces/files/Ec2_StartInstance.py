import boto3

ec2 = boto3.client('ec2', region_name='ap-south-1')

instance_id = 'i-0997c6e8e7102f990'

def start_instance(instance_id):
    print(f"Starting instance {instance_id}...")
    ec2.start_instances(InstanceIds=[instance_id])
    print("Start request sent.")

def get_instance_status(instance_id):
    response = ec2.describe_instances(InstanceIds=[instance_id])
    state = response['Reservations'][0]['Instances'][0]['State']['Name']
    print(f"Instance {instance_id} is currently: {state}")
    return state

get_instance_status(instance_id)
start_instance(instance_id)
