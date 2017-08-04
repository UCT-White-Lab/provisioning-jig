import usb.core

USBP = (usb.TYPE_CLASS | usb.RECIP_OTHER)

def pOff(pNum):
	hubs = usb.core.find(find_all=True, bDeviceClass=usb.CLASS_HUB)
	dev_hub = hubs.next()
	dev_hub.ctrl_transfer(USBP, 1, 8, pNum)

def pOn(pNum):
	hubs = usb.core.find(find_all=True, bDeviceClass=usb.CLASS_HUB)
        dev_hub = hubs.next()
        dev_hub.ctrl_transfer(USBP, 3, 8, pNum)
