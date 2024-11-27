# Write a program to read a file line by line and store each line in a list.

file_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Practice\example.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

print(lines)
