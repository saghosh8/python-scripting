# How can you automate checking if a directory exists and 
# create it if it doesn’t using Python’s os module?

import os

folder_path = r'D:\All Documents\Resume and interview preparation\GitHub\Test Folder'

if not os.path.exists(folder_path):
    os.mkdir(folder_path)    
    print('Folder Created')

else:
    print('Folder Already Exists')