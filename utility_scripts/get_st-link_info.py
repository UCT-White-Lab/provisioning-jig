import usb.core
import time

def byte_str_to_str(line):
    hexs = ['0x' + line[i:i+2] for i in range(0, len(line), 2)]
    byte_ints = [int(h, 16) for h in hexs]
    return "".join(chr(b) for b in byte_ints)

def str_to_byte_str(line):
    l = ''
    for i in range(len(line)):
        l += hex(ord(line[i]))[2:]
        if hex(ord(line[i]))[2:] == '0':
            l += '0'
    return l

def getKey(dev):
    dev.write(0x02, byte_str_to_str('F308'), 100)
    response = dev.read(0x81, 100)
    str = ''
    for c in response:
        str += (chr(c))
    return str_to_byte_str(str)

devices = usb.core.find(find_all=1, idVendor=0x0483, idProduct=0x3748)
for dev in devices:
    print "Found ST-Link V2, id: "# + str_to_byte_str(usb.util.get_string(dev, 3))
    print "Key bytes: " + getKey(dev)
