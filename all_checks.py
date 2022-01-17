#!/usr/bin/env python3
import os
import sys

def check_reboot():
    """Return True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_absolute, min_percent):
    """Returns True if there is enough free disk space, false otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the perecentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free/2**30
    if percent_free < min_percent or gigabytes_free < min_absolute:
        return False
    return True

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    if not check_disk_usage("/", 2, 10):
    print("ERROR: Not enough disk space.")
    sys.exit(1)
    
    print("Everything ok.")
    sys.exit(0 )

main()
