# Rename a File

import os

src_file_name = r'\path\to\src_file.txt'
dest_file_name = r'\path\to\dest_file.txt'

if os.path.exists(src_file_name):
    os.rename(src_file_name, dest_file_name)
    print('File Renamed')

else:
    print('Source file does not exist')