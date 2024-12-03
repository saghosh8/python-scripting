# Copy Files by Extension

import os
import sys
import shutil

if len(sys.argv) < 4:
    print("Usage: python script.py <source_folder> <destination_folder> <extension>")
    sys.exit(1)

source_folder = sys.argv[1]
destination_folder = sys.argv[2]
extension = sys.argv[3]

for filename in os.listdir(source_folder):
    if filename.endswith(extension):
        shutil.copy(os.path.join(source_folder, filename), destination_folder)

print("Files copied successfully!")