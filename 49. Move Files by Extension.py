# Move Files by Extension

import sys
import os
import shutil

src_folder = sys.argv[1]
dest_folder = sys.argv[2]
ext = sys.argv[3]

if len(sys.argv) !=4:
    print("Usage: Python.py <source dir> <dest Dir> <ext>")
    exit(1)

for files in os.listdir(src_folder):
    if files.endswith(ext):
        file_path1 = os.path.join(src_folder, files)
        file_path2 = os.path.join(dest_folder, files)
        shutil.move(file_path1, file_path2)