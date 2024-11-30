# Automate copying new files to another location using shutil.

import shutil
import os

src_dir = r'/path/to/src_dir'
dest_dir = r'/path/to/dest_dir'

# Ensure the destination directory exists
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Loop through files in the source directory
for file in os.listdir(src_dir):
    src_file = os.path.join(src_dir, file)
    dest_file = os.path.join(dest_dir, file)
    
    # Check if it's a file
    if os.path.isfile(src_file):
        # Copy the file
        shutil.copy2(src_file, dest_file)  # copy2 preserves metadata
        print(f"Copied: {file}")
