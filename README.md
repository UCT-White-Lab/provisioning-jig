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
