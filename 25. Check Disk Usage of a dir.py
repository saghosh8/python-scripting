# Check Disk Usage of a dir

import os
import shutil

dir_name = r'\path\to\the\dir'

if os.path.exists(dir_name):
    Usage = shutil.disk_usage(dir_name)
    print(f'Total: {Usage.total}/(1024**3), Free: {Usage.free}/(1024**3), Used: {Usage.used}/(1024**3)')
else:
    print("Path doesnt exists")