# Move Files Based on Types

import os
import shutil

src_dir = 'folder1'
dest_dir = 'folder2'

for files in os.listdir(src_dir):
    src_file_path = os.path.join(src_dir, files)
    dest_file_path = os.path.join(dest_dir, files)
    if os.path.isfile(src_file_path) and files.endswith("log"):
        shutil.move(src_file_path, dest_file_path)