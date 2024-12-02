# Check disk usage and alert if it exceeds 90%


import shutil

usage = shutil.disk_usage('.')
if (usage.used / usage.total )*100 > 90:
    print("Critical")
else:
    print("Green")