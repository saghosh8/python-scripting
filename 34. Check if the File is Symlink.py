# Check if the File is Symlink

import os

file_path = r'\path\to\file_or_symlink'

if os.path.islink(file_path):
    print(f"{file_path} is a symlink.")
else:
    print(f"{file_path} is not a symlink.")
