# Check Disk Usage

import shutil

usage = shutil.disk_usage("/")

print(f"Total: {usage.total/(1024**3):.2f}GB")
print(f"Used: {usage.used/(1024**3):.2f}GB")
print(f"Free: {usage.free/(1024**3):.2f}GB")
print(f"Percent: {(usage.used/usage.total)*100}%")

# Another Way:

import psutil

partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"partition: {partition.device}")
    usage = psutil.disk_usage(partition.mountpoint)
    print(f"Total: {usage.total/(1024**3):.2f}GB")
    print(f"Used: {usage.used/(1024**3):.2f}GB")
    print(f"Free: {usage.free/(1024**3):.2f}GB")
    print(f"Percent: {(usage.used/usage.total)*100}%")