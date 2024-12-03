# Backup Files by Copying

import os
import sys
import shutil

if len(sys.argv) < 3:
    print("Usage: python script.py <source_folder> <backup_folder>")
    sys.exit(1)

source_folder = sys.argv[1]
backup_folder = sys.argv[2]


for filename in os.listdir(source_folder):
    src_path = os.path.join(source_folder, filename)
    backup_path = os.path.join(backup_folder, filename)
    if os.path.isfile(src_path):
        shutil.copy(src_path, backup_path)

print("Backup completed successfully!")