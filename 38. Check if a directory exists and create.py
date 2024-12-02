# Check if a directory exists and create it if it doesn’t using `os`

import os

dir = r'\path\to\folder'

if os.path.exists(dir):
    print("Dir Exists")
else:
    os.mkdir(dir)
    print("Dir Created")