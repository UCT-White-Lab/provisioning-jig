# provisioning-jig
Code and design files for a jig designed to program the STM32 dev boards used for Intro to Micros


CAD Models: Very much in progress, and not much here yet

pcb: Also just starting, with a schematic in progress

utility_scripts: Mainly for development on laptop - used for development and HW testing

fw_update: upgrade_fw.py is my re-write of STs upgrade util. st1_run and st2_run
are usb traffic captures and some files. The java stuff is mainly based on some of the
decompiled code from the updater, doing the crypto stuff. If I have time I'd like to re-write THIS
in python but since it works, we're probably stuck with it.





Setting up the pi:

Install raspbian. Set it up to start ssh (make a new, blank file named 'ssh' in the root dir)
Install pip, then pip install pexpect, ###
Install java (sudo apt-get install oracle-java7-jdk)
Install git.
git clone ###
copy in the fw files and that all important hex


How this all works

The Pi runs the show. One USB cable connects to an ST-link v2, which is used to
program the demo elf onto the targets and the DFU hex onto the soon-to-be debuggers.
In both cases, the chips are flashed in the follwoing way:
1) OpenOCD is Started
2) A telnet connection is established with OpenOCD
3) Through this telnet connection, halt, erase, load etc are called
4) Everything is closed down

A DFU firmware does not a debugger make, so there is another stage required to turn
what is essentially just an STM32F1 into a fancy stlink-v2. We need to run the firmware
update tool from ST. Unfortunately, it doesn't work on the pi. What we probably should
have done is just slap something else with an x86 processor in there. Instead, I
went the fun route. upgrade_fw.py talks USB to the DFU code on the debug board, putting it
in upgrade mode, getting a unique string of bytes from the device, encrypting that, using the
encrypted bytes as a key to encrypt the firmware, sending said firmware in 1024 byte chunks as
USB bulk transfers (with some extra coms to tell the chip where we want them written and give it
some checksums) and finishing up with a last few USB exchanges to write the new FW version etc.
