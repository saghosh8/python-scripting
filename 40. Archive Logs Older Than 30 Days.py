# Archive Logs Older Than 30 Days

import os
from datetime import datetime, timedelta
import shutil

src_dir = 'logs'
dest_dir = r'logs\backup'
older_time = timedelta(days=30)

for files in os.listdir(src_dir):
    src_path = os.path.join(src_dir, files)
    dest_path = os.path.join(dest_dir, files)
    if os.path.isfile(src_path):
        modified_time = datetime.fromtimestamp(os.path.getmtime(src_path))
        current_time = datetime.now()
        if (current_time - modified_time) > older_time:
            shutil.make_archive(dest_dir, '.zip', src_dir)