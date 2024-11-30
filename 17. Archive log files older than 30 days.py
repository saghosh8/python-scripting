# Archive log files older than 30 days.

import os
import shutil
from datetime import datetime, timedelta

dir = "logs"
cutoff_date = datetime.now() - timedelta(days=30)

# Loop through the files in the directory
for file in os.listdir(dir):
    file_path = os.path.join(dir, file)
    if os.path.isfile(file_path):
        # Get the file's creation time
        file_creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
        
        # Check if the file's creation time is older than 30 days
        if file_creation_time < cutoff_date:
            # Create a zip archive for the directory
            shutil.make_archive('backup', 'zip', dir)
            print("Backup Created")
