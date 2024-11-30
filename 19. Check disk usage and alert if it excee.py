# Check disk usage and alert if it exceeds 90%.

import shutil

dir = '/'

usage = shutil.disk_usage(dir)
if (usage.used/usage.total) * 100 > 90:
    print("Critical")
