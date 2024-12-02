# Delete File if It Exists

import os

file_name = r'\path\to\sample.txt'

if os.path.exists(file_name):
    os.remove(file_name)
    print('File Deleted')