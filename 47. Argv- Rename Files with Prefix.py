# 47. Argv- Rename Files with Prefix

import sys
import os

src_folder = sys.argv[1]
prefix = sys.argv[2]


if len(sys.argv) !=3:
    exit(1)
 
for files in os.listdir(src_folder):
    file_path = os.path.join(src_folder, files)
    if os.path.isfile(file_path):
        new_file_name = os.path.join(src_folder, prefix + '_' + files)
        os.rename(file_path, new_file_name)