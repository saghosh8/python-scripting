# Sort Files into Subfolders by Extension

import os
import shutil
import sys

src_folder = sys.argv[1]
dest_folder = sys.argv[2]
ext = sys.argv[3]

if len(sys.argv) != 4:
    print(f"Usage: Script.py src_folder Dest_folder ext")
    exit(1)

for files in os.listdir(src_folder):
    if files.endswith(ext):
        src_file_path = os.path.join(src_folder, files)
        new_folder = os.path.join(dest_folder, ext.lstrip('.'))
        os.makedirs(new_folder, exist_ok=True)
        dest_file_path = os.path.join(new_folder, files)
        shutil.copy(src_file_path, dest_folder)