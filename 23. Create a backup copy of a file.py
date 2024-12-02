# Create a backup copy of a file

import os
import shutil

src_file_name = r'\path\to\src_file.txt'
dest_file_name = r'\path\to\src_backup_file.txt'

if os.path.exists(src_file_name):
    shutil.copy(src_file_name, dest_file_name)
    print('Backup Taken')
else:
    print("Files Doesnt Exists")