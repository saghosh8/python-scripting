# Schedule a script to run every 24 hours.

import schedule
import time

def my_script():
    print("Running the script!")
schedule.every(24).hours.do(my_script)

while True:
    schedule.run_pending()
    time.sleep(1)