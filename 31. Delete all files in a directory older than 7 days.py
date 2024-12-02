# Delete all files in a directory older than 7 days.

import os
import time

dir_name = r"\path\to\folder"
now = time.time()

if os.path.exists(dir_name):
    for files in os.listdir(dir_name):
        file = os.path.join(dir_name, files)
        if os.path.isfile(file) and (now - os.path.getmtime(file)) > 7 * 86400:
            os.remove(file)
else:
    print('dir doesnt exists')

# Another way
import os
import time
from datetime import datetime, timedelta

dir_name = r"\path\to\folder"
now = datetime.now()

if os.path.exists(dir_name):
    for file in os.listdir(dir_name):
        file_path = os.path.join(dir_name, file)
        if os.path.isfile(file_path):
            file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            if now - file_mod_time > timedelta(days=7):
                os.remove(file_path)
                print(f"Deleted: {file}")
else:
    print('Directory does not exist')
