# 18. Delete Temporary Files

import os

dir = "temp"

for file in os.listdir(dir):
    files = os.path.join(dir, file)
    if os.path.isfile(files):
        os.remove(files)
        print("files deleted")