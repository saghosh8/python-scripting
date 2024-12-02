# 48. Argv- Rename Files with Suffix

import sys
import os

src_folder = sys.argv[1]
suffix = sys.argv[2]


if len(sys.argv) !=3:
    exit(1)
 
for files in os.listdir(src_folder):
    file_path = os.path.join(src_folder, files)
    if os.path.isfile(file_path):
        new_file_name = os.path.join(src_folder, files + '_' + suffix)
        os.rename(file_path, new_file_name)