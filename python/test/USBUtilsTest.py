import sys
sys.path.insert(0, '../')

from USButils import *

devices = getUSBDevices()

for mount, info in devices.items():
	print(mount)
	print(" ".join(["	Device Number:", info[0]]))
	print(" ".join(["	Device Product:", info[1]]))
	print(" ".join(["	Device Manufacturer:", info[2]]))
