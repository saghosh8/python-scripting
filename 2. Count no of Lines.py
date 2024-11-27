# Write a program to count the number of lines in a file named data.txt.

file_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Practice\example.txt'

with open(file_path, 'r') as file:
    no_of_lines = len(file.readlines())
    print(f'This file has {no_of_lines} Number of lines.')