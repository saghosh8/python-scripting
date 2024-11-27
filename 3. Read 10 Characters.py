# How would you read the first 10 characters of a file? Write a program.

file_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Practice\example.txt'

with open(file_path, 'r') as file:
    no_of_cha = file.read(10)
    print(f'The first 10 characters of this file is- {no_of_cha}')