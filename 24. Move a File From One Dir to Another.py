# Move a File From One Dir to Another

import os
import shutil

src_file_name = r'\path\to\src_file.txt'
dest_dir = r'\backup\folder'

if os.path.exists(src_file_name):
    shutil.move(src_file_name,dest_dir)
    print("File Moved")

else:
    print("File doesnt exists")