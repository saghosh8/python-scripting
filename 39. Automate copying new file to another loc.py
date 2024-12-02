# Automate copying new file to another location using `shutil`.

import shutil
import os

src_dir = r'\path\to\folder'
dest_dir = r'\path\to\folder2'

for file in os.listdir(src_dir):
    
    file1_path = os.path.join(src_dir, file)
    file2_path = os.path.join(dest_dir, file)

    if os.path.isfile(file1_path):
        shutil.copy2(file1_path, file2_path)

