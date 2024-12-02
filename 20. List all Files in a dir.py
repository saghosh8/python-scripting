# List all Files in a dir

import os

# This approach will list all files and Folder
folder_name = r'\path\to\dir'

if os.path.exists(folder_name):
    files = os.listdir(folder_name)
    print(files)
else:
    print("folder doesnt exists")

# This approach will list all files but not Folder
folder_name = r'\path\to\dir'

if os.path.exists(folder_name):
    for root, dirs, files in os.walk(folder_name):
        print(f'Files: {files}')