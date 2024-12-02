# 33. Unzip a file to a specefic directory.

import shutil
dir_name = '.'
backup = r'\path\to\zip\backup.zip'
shutil.unpack_archive(backup, dir_name)