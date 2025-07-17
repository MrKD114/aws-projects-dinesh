import boto3

def deploy_stack(stack_name, template_path):
    cf = boto3.client('cloudformation', region_name='ap-south-1')

    with open(template_path, 'r', encoding='utf-8') as file:
        template_body = file.read()

    try:
        print(f"Creating stack: {stack_name}")
        response = cf.create_stack(
            StackName=stack_name,
            TemplateBody=template_body,
            Capabilities=[] 
        )

        waiter = cf.get_waiter('stack_create_complete')
        waiter.wait(StackName=stack_name)
        print(f"Stack {stack_name} created successfully.")

    except cf.exceptions.AlreadyExistsException:
        print(f"Stack {stack_name} already exists.")
    except Exception as e:
        print("Failed to create stack:", e)


StackName = input("Please enter the stack name : ")
deploy_stack(StackName, 'dynamo-db-template.yaml')