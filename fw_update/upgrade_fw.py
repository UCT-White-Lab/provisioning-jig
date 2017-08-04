import usb.core
import time
import pexpect
import re
import os
import subprocess

#### SET THIS ONCE - FOR THE BUILT IN ST-LINK ####
#### Use get_st-link_info.py to print this out ###
stlinkID = "52ff68067188485525600367"#""

wd = os.path.dirname(os.path.realpath(__file__))

def byte_str_to_str(line):
    hexs = ['0x' + line[i:i+2] for i in range(0, len(line), 2)]
    byte_ints = [int(h, 16) for h in hexs]
    return "".join(chr(b) for b in byte_ints)

def str_to_byte_str(line):
    l = ''
    for i in range(len(line)):
        if ord(line[i]) < 10:
            l += '0'
        l += hex(ord(line[i]))[2:]
    return l

def getKey(dev):
    dev.write(0x02, byte_str_to_str('F308'), 100)
    response = dev.read(0x81, 100)
    str = ''
    for c in response:
        str += (chr(c))
    return str_to_byte_str(str)

key = ''

devices = usb.core.find(find_all=1, idVendor=0x0483, idProduct=0x3748)
debug = None
for dev in devices:
    # This doesn't work on the pi - check out those udev rules? It also needs to run as root
    #idstr = str_to_byte_str(usb.util.get_string(dev, 3))
    key = getKey(dev)
    print "Found ST-Link V2, id: " #+ idstr
    print "Key bytes: " + key
    debug = dev


if debug == None:
    print "No Device attached!!!"


# We need to decrypt the firmware, reencrypt it, split it up into chunks and
# send them to the device.

# These are the bytes sent by the device, used to dynamically encrypt the fw
# Thoery: it's a set first four bytes + the device ID?
key16 = byte_str_to_str(key)[:4]+byte_str_to_str(key)[8:]
f308 = open(wd+"/f303_bytes_4_12.bin", "wb")
f308.write(key16)
f308.close()

# We use some java, from the update utility (decompiled, stripped down and recompiled)
# It looks for the f308 file created above
subprocess.Popen('java -jar STDecrypt.jar', cwd=wd, shell=True)
# If it worked, there should be a file named fw_re_encrypted.bin in this directory
time.sleep(1) # Give the jar time to execute? Not sure this is needed
if (os.path.isfile(wd+'/fw_re_encrypted.bin')):
    print "success"
else:
    print "fail"

bin_file = wd+'/fw_re_encrypted.bin'
fstr = open(wd+"/version_thingee_16.bin", 'rb').read()

# Make the address commands
address_cmds = []
for i in range(0x40, 0xb8, 0x04):
    address_cmds.append('2100'+str(hex(i))[2:] + '0008')
print len(address_cmds)

fw_chunks = []
bf = open(bin_file, 'rb')
for i in range(30): # There are 30 1kB chunks
    fw_chunks.append(bf.read(1024))
print len(fw_chunks)

# For now, steal the checksums from the USB data cap - it's the same in all cases (must be pre-encryption?)
# Apparently the checksums are sums of all the data sent? Who knows
fw_write_cmds = [
    'f3010200648d00040000000000000000',
    'f3010300a4a700040000000000000000',
    'f3010400949500040000000000000000',
    'f3010200a2ce00040000000000000000',
    'f301030072ad00040000000000000000',
    'f30104006c7500040000000000000000',
    'f3010200eab500040000000000000000',
    'f3010300eac000040000000000000000',
    'f3010400efc400040000000000000000',
    'f30102005d9d00040000000000000000',
    'f3010300beb400040000000000000000',
    'f30104003e9b00040000000000000000',
    'f30102006ca100040000000000000000',
    'f3010300979400040000000000000000',
    'f3010400116c00040000000000000000',
    'f3010200e79800040000000000000000',
    'f3010300be8d00040000000000000000',
    'f30104001b6a00040000000000000000',
    'f3010200d1a800040000000000000000',
    'f3010300735600040000000000000000',
    'f3010400ea9b00040000000000000000',
    'f3010200928400040000000000000000',
    'f3010300699100040000000000000000',
    'f3010400219600040000000000000000',
    'f3010200b58000040000000000000000',
    'f30103005bb800040000000000000000',
    'f3010400316100040000000000000000',
    'f30102005caa00040000000000000000',
    'f3010300296500040000000000000000',
    'f3010400316100040000000000000000',
    'f301020061f000040000000000000000']

# These are sent at the start, querying version and setting up in firmware update mode
start_commands = [
    ['f1800000000000000000000000000000', 1],
    ['f5000000000000000000000000000000', 1],
    ['f3010000450105000000000000000000', 0],
    ['4100fc0008',2],
    ['f3010000180205000000000000000000',0],
    ['21f0ff0008',2],
    ['f3010200f00f10000000000000000000',0],
    ['5c971a46af77599b8098da64ebe5ff69',2],
    ['f3010000890005000000000000000000',0],
    ['4100400008',2],
    ['f30100008d0005000000000000000000',0],
    ['4100440008',2],
    ['f3010000910005000000000000000000',0],
    ['4100480008',2]
]

def wait_for_ready():
    dev.write(0x02, byte_str_to_str('f3030000000006000000000000000000'), 100)
    response = dev.read(0x81, 100)
    print response
    while response[4] == 4:
        time.sleep(0.1) # wait a little bit longer
        dev.write(0x02, byte_str_to_str('f3030000000006000000000000000000'), 100)
        response = dev.read(0x81, 100)
    if response[4] == 2:
        time.sleep(0.2)

# And awaaay we go

# Start commands
for c in start_commands:
    # print c
    dev.write(0x02, byte_str_to_str(c[0]), 100)
    if c[1] == 3:
        a = dev.read(0x81, 100)
        wait_for_ready()
    if c[1] == 2:
        wait_for_ready()
    if c[1] == 1:
        a = dev.read(0x81, 100)

# Send the packets
for i in range(30):
    # print i
    wait_for_ready()

    dev.write(0x02, byte_str_to_str("f3010000"+ hex(0x69 + 4*i)[2:] + "0005000000000000000000"))
    print "wrote command: ", ("f3010000"+ hex(0x69 + 4*i)[2:] + "0005000000000000000000")
    add_cmd_str = byte_str_to_str(address_cmds[i])
    dev.write(0x02, add_cmd_str,1000)
    print "Wrote addr:", str_to_byte_str(add_cmd_str)

    wait_for_ready()

    fw_str = byte_str_to_str(fw_write_cmds[i])
    dev.write(0x02, fw_str, 1000)
    print "Wrote fw command: ", str_to_byte_str(fw_str)

    fw_chunk = fw_chunks[i] # No need to convert
    dev.write(0x02, fw_chunk, 1000)
    print "Wrote firmware chunk", i

wait_for_ready()
dev.write(0x02, byte_str_to_str("f3010000450105000000000000000000"), 100)
dev.write(0x02, byte_str_to_str("4100fc0008"), 100)
print "Wrote stuff"
wait_for_ready()
time.sleep(0.5)

dev.write(0x02, byte_str_to_str("f3010000180205000000000000000000"), 100)
dev.write(0x02, byte_str_to_str("21f0ff0008"), 100)

print "Wrote stuff"

wait_for_ready()


dev.write(0x02, byte_str_to_str("f3010200930d10000000000000000000"), 100)
# This bit is also encrypted by STDecrypt think it's the firmware version
dev.write(0x02, fstr, 100) # "1152a590a0cf13fd7e66d64915d5c5bd" This is unique to each device - investigate!!!

print "wrote stuff"
wait_for_ready()

# Get FW and print
dev.write(0x02, byte_str_to_str("f3070000000000000000000000000000"), 100)
dev.write(0x02, byte_str_to_str("f1800000000000000000000000000000"), 100)
print dev.read(0x81, 100)
