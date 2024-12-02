# Find Files with specific ext

import os

dir_name = r'\path\to\folder'
ext = ".txt"

for file in os.listdir(dir_name):
    if file.endswith(ext):
        print(file)   