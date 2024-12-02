# Recursively list all files and folders in a directory.

import os

# One way to do
dir_name = r'\path\to\dir'

if os.path.exists(dir_name):
    list = os.listdir(dir_name)
    print(list)

else:
    print('Dir doesnt exists')

# Another way to do
dir_name = r'\path\to\dir'

for root, dirs, files in os.walk(dir_name):
    print(f'root: {root},
            Folders: {dirs},
            Files: {files}')