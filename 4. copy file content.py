# Write a program to copy the contents of one file to another.

src_file = r'D:\All Documents\Resume and interview preparation\GitHub\Python Practice\example.txt'
dest_file = r'D:\All Documents\Resume and interview preparation\GitHub\Python Practice\example-2.txt'

with open(src_file, 'r') as file:
    content = file.read()

with open(dest_file, 'w') as dest:
    dest.write(content)
    print('file copied successfully')