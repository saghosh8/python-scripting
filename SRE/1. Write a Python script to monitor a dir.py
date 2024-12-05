# Write a Python script to monitor a directory and log any changes (new files added, files deleted, or modified). 
# Include error handling to ensure the script continues running even if an exception occurs.

import os
import time

dir_path = r'\path\to\dir'

before = set(os.listdir(dir_path))

while True:
    try:
        after = set(os.listdir(dir_path))

        added = after - before
        removed = before - after

        if added:
            print(f"Below Files are Added")
            print(f"{added}")
        elif removed:
            print(f"Below Files are Removed")
            print(f"{removed}")
        before = after
        time.sleep(5)

    except Exception as e:
        print(f"Error: {e}")
        continue
