# Write a program to create a new file test.txt and 
# write the text "Python is fun!" into it.

file_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Practice\example.txt'

with open(file_path, 'w') as file:
    file.write('Python is fun!')
    print('File Created Successfully')