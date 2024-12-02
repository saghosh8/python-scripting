# Create Symlink to a File

import os

src = r'sourceFolder\file.txt'
dest = r'destFolder\file2.txt'

os.symlink(src,dest)
