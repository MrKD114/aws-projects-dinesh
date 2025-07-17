import zipfile
import os

current_dir = os.getcwd()
zip_file_path = os.path.join(current_dir,"lambda_function.zip")
source_file = os.path.join(current_dir, "lambda_function.py")

def Zipper():
    try :
        with zipfile.ZipFile(zip_file_path,"w") as zf:
            zf.write(source_file, arcname="lambda_function.py")
        print("Zip file created successfully")
    except Exception as e:
        print(e)
Zipper()