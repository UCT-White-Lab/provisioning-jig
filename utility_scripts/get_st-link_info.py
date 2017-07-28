import usb.core
import time


devices = usb.core.find(find_all=1, idVendor=0x0483, idProduct=0x3748)
for dev in devices:
    print "Found ST-Link V2"
    
