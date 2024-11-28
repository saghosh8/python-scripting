import difflib

file1_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Practice\example.txt'
file2_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Practice\merged_file.txt'

with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
    file1_lines = file1.readlines()
    file2_lines = file2.readlines()

# Generate differences
diff = difflib.unified_diff(file1_lines, file2_lines, fromfile='File1', tofile='File2')

# Print differences
for line in diff:
    print(line, end='')
