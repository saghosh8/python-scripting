# Write a program to merge the contents of two files into a third file.

file1_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Practice\example.txt'
file2_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Practice\example-2.txt'
merged_file_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Practice\merged_file.txt'

# Read content from both files
with open(file1_path, 'r') as file1:
    content1 = file1.read()

with open(file2_path, 'r') as file2:
    content2 = file2.read()

# Merge content and write to the third file
with open(merged_file_path, 'w') as merged_file:
    merged_file.write(content1 + "\n" + content2)

print("Contents of both files merged successfully.")
