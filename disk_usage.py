#!/usr/bin/env python3
import shutil
import sys
import os

def check_reboot():
	""" Returns True if the computer has a pending reboot """
	return os.path.exists("/run/reboot-required")

def check_disk_usage(disk, min_absolute, min_percent):

	du = shutil.disk_usage(disk)
	# Calculate percentage of free space
	percent_free = 100 * du.free / du.total
	
	gigabytes_free = du.free * 2**30
	
	if percent_free < min_percent or  gigabytes_free < min_absolute:
		return False
	return True
if not check_disk_usage("/",2*2**30, 10):
	print("ERROR: Not enough disk space.")
	sys.exit(1)
print("Everything ok.")
sys.exit(0)
