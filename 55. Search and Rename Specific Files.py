# Search and Rename Specific Files

import os
import shutil
import sys

src_folder = sys.argv[1]
keyword = sys.argv[2]
new_keyword = sys.argv[3]

if len(sys.argv) != 4:
    print(f"Usage: Script.py src_folder keyword new_keyword")
    exit(1)

for files in os.listdir(src_folder):
    if keyword in files:
        old_path = os.path.join(src_folder, files)
        new_path = os.path.join(src_folder, files.replace(keyword, new_keyword))
        os.rename(old_path, new_path)