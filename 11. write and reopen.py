# Write a program to create a file, write some data, and then reopen it in read mode to display the data.

file_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Practice\example-3.txt'

# Create and write data to the file
with open(file_path, 'w') as file:
    file.write("Write a program to create a file, write some data, and then reopen it in read mode to display the data.")

# Reopen the file in read mode and display its content
with open(file_path, 'r') as file:
    content = file.read()
    print(content)
