# Measure the time taken by a script to execute.

import time

start_time = time.time()
time.sleep(10)
end_time = time.time()

time_taken = end_time - start_time
print(time_taken)