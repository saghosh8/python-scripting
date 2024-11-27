# How would you handle encoding errors while reading a file?

file_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Practice\example.txt'

with open(file_path, 'r', errors='ignore') as file:
    content = file.read()

print(content)


# 'ignore': Ignores characters that cause encoding errors.
# 'replace': Replaces invalid characters with a replacement character (usually '�').
# 'strict': Raises a UnicodeDecodeError (default).