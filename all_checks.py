#!/usr/bin/env python3


import os
import shutil
import sys

def check_reboot():
	""" Return True if the computer has a pendng reboot file """
	return os.path.exists("/run/reboot-required")


def check_disk_usage(disk, min_gb, min_percent):

        du = shutil.disk_usage(disk)
        # Calculate percentage of free space
        percent_free = 100 * du.free / du.total

        gigabytes_free = du.free / 2**30
        if percent_free < min_percent or  gigabytes_free < min_gb:
                return False
        return True
def main():
	if check_reboot():
		print("Pending Reboot")
		sys.exit(1)
	
	if not check_disk_usage(disk="/",min_gb=2,min_percent= 10):
        	print("ERROR: Not enough disk space.")
        	sys.exit(1)

	print("Everything is ok.")
	sys.exit(0)
main()
