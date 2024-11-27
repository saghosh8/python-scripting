file_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Scripting\Test-Files\example.txt'

with open(file_path, 'r') as file:
    content = file.read()
    print(content)