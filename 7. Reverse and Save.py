# Write a program to reverse the contents of a file and save it to another file.

src_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Practice\example.txt'
dest_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Practice\example-2.txt'

with open(src_path, 'r') as file:
    content = file.read()

reversed_content = content[::-1]

with open(dest_path, 'w') as dest:
    dest.write(reversed_content)

print('File content reversed and saved successfully.')
