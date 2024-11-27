# Write a program to check if a file is empty.

file_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Practice\example.txt'

with open(file_path, 'r') as file:
    content = file.read()

if not content:
    print('The file is empty.')
else:
    print('The file is not empty.')
