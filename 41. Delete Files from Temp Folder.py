# Delete Files from Temp Folder

import os 

dir = 'temp'

for files in os.listdir(dir):
    file_path = os.path.join(dir, files)
    if os.path.isfile(file_path):
        os.remove(file_path)
