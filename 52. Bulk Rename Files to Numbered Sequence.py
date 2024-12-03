# Bulk Rename Files to Numbered Sequence

import os
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <folder_path>")
    sys.exit(1)

folder_path = sys.argv[1]

# enumerate(..., start=1): Loops through the list of files, 
#with i being the index starting at 1 and files being the file names.
for i, files in enumerate(os.listdir(folder_path), start = 1):

    #os.path.splitext(files): Splits the file name into two parts: 
    #name (the main file name) and ext (the file extension, e.g., .txt).
    name, ext = os.path.splittext(files)
    
    old_path = os.path.join(folder_path, files)
    new_path = os.path.join(folder_path, f'{i}{ext}')
    os.rename(old_path, new_path)
