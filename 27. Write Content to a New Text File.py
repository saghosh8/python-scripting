# Write Content to a New Text File

src_file_name = r'\path\to\src_file.txt'
dest_file_name = r'\path\to\dest_file.txt'

with open(src_file_name, 'r') as file1:
    content = file1.read()

with open(dest_file_name, 'w') as file2:
    file2.write(content)