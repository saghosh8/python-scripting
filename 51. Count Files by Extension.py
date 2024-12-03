# Count Files by Extension

import sys
import os

src_folder = sys.argv[1]
ext = sys.argv[2]

if len(sys.argv) !=3:
    exit(1)

count=0

for files in os.listdir(src_folder):
    file_path = os.path.join(src_folder, files)
    if files.endswith(ext):
        count +=1
print(count)        