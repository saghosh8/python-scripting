# Zip all files in a directory.

import shutil

dir_name = r'\path\to\folder'
backup = r'\path\to\backup_folder'

shutil.make.archive('backup', '.zip', 'dir_name')