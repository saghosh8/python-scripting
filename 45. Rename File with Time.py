# Rename files to include a timestamp.

import os
import time

src = r'\path\to\folder'

for files in os.listdir(src):
    file_path = os.path.join(src, files)
    if os.path.isfile(file_path):
        time_now = time.strftime('%Y-%m-%d %H:%M:%S')
        renamed_file = os.path.join(src, files + '_' + time_now)
        os.rename(file_path, renamed_file)
