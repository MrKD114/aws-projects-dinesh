import boto3
IAM = boto3.client('iam')
def CreateIAMuser(UserName):
    try:
        IAM.create_user(UserName = UserName)
        print(f"Successfully created user {UserName}")
    except Exception as e:
        print(e)

def AttachPolicyToUser(Username, PolicyArn):
    try:
        IAM.attach_user_policy(UserName = Username, PolicyArn = PolicyArn)
        print(f"IAMReadOnlyAccess Policy attached to {Username}")
    except Exception as e:
        print(e)

UserNameInp = input("Please enter user name : ")
PolicyArn = 'arn:aws:iam::aws:policy/IAMReadOnlyAccess'

CreateIAMuser(UserNameInp)
AttachPolicyToUser(Username=UserNameInp, PolicyArn=PolicyArn)