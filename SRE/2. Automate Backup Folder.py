# Write a Python script to automate the backup of a folder to a designated backup location.
# The script should create a timestamped folder for each backup 
# and ensure that any previous backup is not overwritten.
# Include error handling to handle file system errors.
# The script can be set to run once every 24 hours.

import shutil
from datetime import datetime
import schedule
import time

def backup_script():
    try:
        src_folder = r"D:\All Documents\Resume and interview preparation\GitHub\Python Practice"
        dest_folder = r"D:\All Documents\Resume and interview preparation\GitHub"
        time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        backup_folder = f"{dest_folder}_{time_now}"

        shutil.copytree(src_folder, backup_folder)
        
    except Exception as e:
        print(f"Error: {e}")


schedule.every(24).hours.do(backup_script)

while True:
    schedule.run_pending()
    time.sleep(1)