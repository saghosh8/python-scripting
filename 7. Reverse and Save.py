# Write a program to reverse the contents of a file and save it to another file.

src_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Practice\example.txt'
dest_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Practice\example-2.txt'
#Open file and store content
with open(src_path, 'r') as file:
    content = file.read()
#Reverse the Content
reversed_content = content[::-1]
#Save the Content in Another File
with open(dest_path, 'w') as dest:
    dest.write(reversed_content)

print('File content reversed and saved successfully.')