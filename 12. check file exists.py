# Write a program to check if a file exists before trying to open it.


import os

file_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Practice\example.txt'

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
else:
    print(f"The file at {file_path} does not exist.")
