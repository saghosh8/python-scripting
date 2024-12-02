# Monitor a directory for changes (new files or deleted files).

import time
import os

dir = 'logs'
before = set(os.listdir(dir))

while True:
    time.sleep(5)
    after = set(os.listdir(dir))
    added = after - before
    removed = before - after
    if added:
        print("added")
    elif removed:
        print("removed")
    before = after
