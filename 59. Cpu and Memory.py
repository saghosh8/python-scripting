#Cpu and Memory

import psutil
memory = psutil.virtual_memory()
print(f" Total Memory: {memory.total / (1024 ** 3):.2f} GB")
print(f" Available Memory: {memory.available / (1024 ** 3):.2f} GB")
print(f" Memory Usage: {memory.percent}%")


# Get current CPU usage percentage
cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_usage}%")