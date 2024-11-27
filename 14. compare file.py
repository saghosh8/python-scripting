# Write a program to compare two files line by line and display differences.

file1_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Practice\example.txt'
file2_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Practice\merged_file.txt'

# Open both files and read lines
with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
    file1_lines = file1.readlines()
    file2_lines = file2.readlines()

# Compare line by line and display differences
for line_num, (line1, line2) in enumerate(zip(file1_lines, file2_lines), 1):
    if line1 != line2:
        print(f"Difference at line {line_num}:")
        print(f"File1: {line1.strip()}")
        print(f"File2: {line2.strip()}")
        print()
        
# Handle case where one file is longer than the other
if len(file1_lines) > len(file2_lines):
    for line_num in range(len(file2_lines), len(file1_lines)):
        print(f"File1 has extra line {line_num + 1}: {file1_lines[line_num].strip()}")
elif len(file2_lines) > len(file1_lines):
    for line_num in range(len(file1_lines), len(file2_lines)):
        print(f"File2 has extra line {line_num + 1}: {file2_lines[line_num].strip()}")
