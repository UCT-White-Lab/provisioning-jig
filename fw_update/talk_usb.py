import usb.core
import time

# Find the st link
dev = usb.core.find(idVendor=0x0483, idProduct=0x3748)
# configuration = dev.get_active_configuration()
# print configuration
#
# dev.set_configuration()


# # We senf 0xf308, and the chip responds with 20 bytes. The first four and last 12
# # are encrypted with key "best performance", then the 16 encrypted bytes are used
# # as a key to encrypt the firmware before sending it
# byte_ints = [0xf3, 0x08]
# byte_str = "".join(chr(n) for n in byte_ints)
# dev.write(0x02, byte_str)
# response = dev.read(0x81, 100)
# # response = [64, 0, 255, 255, 74, 6, 55, 5, 82, 255, 104, 6, 113, 136, 72, 85, 37, 96, 3, 103]
# print response
# key_bytes = response[:4] + response[8:]
# # print len(key_bytes)




# Now we want to send the re-encrypted firmware, in 1024 byte chunks
# Telling it where to write to, we send 2100400008
# incrementing each block (to 2100440008, 48, 4c, 50 etc)
# (After the first three, it does three starting with 41 in a row (no data transfers) then the same three
# with 21 and a chink of data. There are some others with 41. My theory is that these are erase ops or something
# - and possibly the initial few are getting rid of some sort of protection? <<< needs more investigation
# It proceeds incrementally with each block of fw data up to 2100b40008, then
# the last block goes to 21003c0008?

# The we send f3 (DFU command) 01 (firmware chunk up next) XX (count, 02, 03, 04 then back to 02)
# 00, XXXX (checksum - sum of all bytes being sent) 04 (for size of firmware chunk = 0x0400)

# Finally, we send 1024 bytes of the encrypted firmware

# Make the address commands
address_cmds = []
for i in range(0x40, 0xb8, 0x04):
    address_cmds.append('2100'+str(hex(i))[2:] + '0008')
address_cmds.append('21003c0008')
# print address_cmds

# For now, steal the checksums and actual data from the USB data cap
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
'f301020061f000040000000000000000'
]


fw_chunks = []
bin_file = '/home/jonathan/stm_jig/usb_sniff/bin_chunks.bin'
bin_chunks_concat = open(bin_file, "r")
for i in range(31):
    fw_chunks.append(bin_chunks_concat.read(1024))
    if i!= 30:
        bin_chunks_concat.read(192) # the pcap nonsense inbetween each chunk
# print hex(ord(fw_chunks[1][0])) # just checking it works
#
# print len(address_cmds)
# print len(fw_write_cmds)

def byte_str_to_str(line):
    hexs = ['0x' + line[i:i+2] for i in range(0, len(line), 2)]
    byte_ints = [int(h, 16) for h in hexs]
    return "".join(chr(b) for b in byte_ints)

def str_to_byte_str(line):
    # messes up 00  (puts it to 0)
    l = ''
    for i in range(len(line)):
        l += hex(ord(line[i]))[2:]
        if hex(ord(line[i]))[2:] == '0':
            l += '0'

    return l

# print str_to_byte_str(fw_chunks[0])


# Some setup - not sure what this does!!!
start_commands = [
['f1800000000000000000000000000000', 1],
['f5000000000000000000000000000000', 1],
['f3080000000000000000000000000000', 2],
['f3030000000006000000000000000000', 1],
['f3030000000006000000000000000000', 1],
['f3010000450105000000000000000000', 0],
['4100fc0008',0],
['f3030000000006000000000000000000', 1],
['f3030000000006000000000000000000', 1],
['f3030000000006000000000000000000', 1],
['f3010000180205000000000000000000',0],
['21f0ff0008',0],
['f3030000000006000000000000000000', 1],
['f3030000000006000000000000000000', 1],
['f3010200f00f10000000000000000000',0],
['5c971a46af77599b8098da64ebe5ff69',0],
['f3030000000006000000000000000000', 1],
['f3030000000006000000000000000000', 1],
['f3030000000006000000000000000000', 1],
['f3030000000006000000000000000000', 1],
['f3010000890005000000000000000000',0],
['4100400008',0],
['f3030000000006000000000000000000', 1],
['f3030000000006000000000000000000', 1],
['f30100008d0005000000000000000000',0],
['4100440008',0],
['f3030000000006000000000000000000', 1],
['f3030000000006000000000000000000', 1],
['f3010000910005000000000000000000',0],
['4100480008',0],
['f3030000000006000000000000000000', 1],
]

for c in start_commands:
    dev.write(0x02, byte_str_to_str(c[0]), 100)
    if c[1]==1:
        print dev.read(0x81, 100)
    if c[1] == 2:
        print dev.read(0x81, 100)
    time.sleep(0.06) # simulate encryption stuff

# Send the packets
for i in range(31):
    print i

    dev.write(0x02, byte_str_to_str("f3030000000006000000000000000000"),1000)
    response = dev.read(0x81, 100)
    print response
    dev.write(0x02, byte_str_to_str("f3030000000006000000000000000000"),1000)
    response = dev.read(0x81, 100)
    print response
    count = 0
    while response[4] == 4 and count < 10:
        dev.write(0x02, byte_str_to_str("f3030000000006000000000000000000"),1000)
        response = dev.read(0x81, 100)
        count += 1
        time.sleep(0.1)
        print response

    dev.write(0x02, byte_str_to_str("f3010000"+ hex(0x69 + 4*i)[2:] + "0005000000000000000000"))
    print "wrote command: ", ("f3010000"+ hex(0x69 + 4*i)[2:] + "0005000000000000000000")
    add_cmd_str = byte_str_to_str(address_cmds[i])
    dev.write(0x02, add_cmd_str,1000)
    print "Wrote addr:", str_to_byte_str(add_cmd_str)

    dev.write(0x02, byte_str_to_str("f3030000000006000000000000000000"),1000)
    print dev.read(0x81, 100)
    dev.write(0x02, byte_str_to_str("f3030000000006000000000000000000"),1000)
    print dev.read(0x81, 100)

    fw_str = byte_str_to_str(fw_write_cmds[i])
    dev.write(0x02, fw_str, 1000)
    print "Wrote fw command: ", str_to_byte_str(fw_str)

    fw_chunk = fw_chunks[i] # No need to convert
    dev.write(0x02, fw_chunk, 1000)
    print "Wrote firmware chunk", i

# Finally, write the new version number and stuff like that
def wait_for_ready():
    dev.write(0x02, byte_str_to_str("f3030000000006000000000000000000"),1000)
    response = dev.read(0x81, 100)
    print response
    count = 0
    while response[4] == 4 and count < 10:
        dev.write(0x02, byte_str_to_str("f3030000000006000000000000000000"),1000)
        response = dev.read(0x81, 100)
        count += 1
        time.sleep(0.1)
        print response

wait_for_ready()
dev.write(0x02, byte_str_to_str("f3010000450105000000000000000000"), 100)
dev.write(0x02, byte_str_to_str("4100fc0008"), 100)
print "Wrote stuff"
wait_for_ready()

dev.write(0x02, byte_str_to_str("f3010000180205000000000000000000"), 100)
dev.write(0x02, byte_str_to_str("21f0ff0008"), 100)

print "Wrote stuff"

wait_for_ready()

dev.write(0x02, byte_str_to_str("f3010200930d10000000000000000000"), 100)
dev.write(0x02, byte_str_to_str("f76af84e192bb6f8ce4e6366cfc05f29"), 100)

print "wrote stuff"
wait_for_ready()

# Get FW and print
dev.write(0x02, byte_str_to_str("f3070000000000000000000000000000"), 100)
dev.write(0x02, byte_str_to_str("f1800000000000000000000000000000"), 100)
print dev.read(0x81, 100)
