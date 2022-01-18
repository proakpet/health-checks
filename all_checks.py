#!/usr/bin/env python3
import os
import sys
import shutil

def check_reboot():
    """Return True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    """Returns True if there is enough free disk space, false otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the perecentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free/2**30
    if gigabytes_free < min_gb or percent_free < min_percent:
        return True
    return False

def check_root_full():
    """Return True if the root partition is full, Flase otherwise."""
    return check_disk_full(disk="/", min_gb=2, min_percent=10)

def main():
    checks = [
        (check_reboot, "Pendint Reboot"),
        (check_root_full, "Root partition full"),
    ]
    for check, msg in checks:
        if check():
            print(msg)
            sys.exit(1)

    print("Everything ok.")
    sys.exit(0 )

main()
