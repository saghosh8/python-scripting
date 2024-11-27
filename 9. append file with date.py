# Modify the program to append current date and time to a file every time it is executed.

from datetime import datetime

old_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Practice\example.txt'

current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(old_path, 'a') as file:
    file.write(f"Current Date and Time: {current_date_time}\n")

print('Current date and time appended successfully.')