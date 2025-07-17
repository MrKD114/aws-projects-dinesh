Code = """
def lambda_handler(event, contect):
    print("Lambda triggered successfully ")
    print("Event :" ,event)
    return(
        'statuscode':200,
        'body': 'Hello from lambda'
    )
"""

with open("lambda_function.py", "w") as f:
    f.write(Code.strip())

print("lambda_function.py created successfully")