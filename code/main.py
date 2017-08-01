# Going to thrown everything in this one file for now, and then split it back out
# as I add in IO, LCD, logging etc.

target_elf = 'ksef' #<<<<<<<<<<<<<<<<<

class logger:
    def __init__():
        # logging.basicConfig(format = "%(asctime)s:" + logging.BASIC_FORMAT)
        # logger = logging.getLogger()
        # logger.setLevel(logging.DEBUG)

    def info(str):
        print "Log Info: "+str
    def warn(str):
        print "Log Info: "+str

class lcd:
    def write(str):
        print "Lcd: " + str

class OpenOCDFailed(Exception):
    pass

class DebugOpenOCD:

    def __init__(self, logger=logging.getLogger(__name__)):
        self.logger = logger
        logging.basicConfig(level=logging.DEBUG)
        self.ocd = pexpect.spawn("openocd -f interface/stlink-v2.cfg -f target/stm32f1x_stlink.cfg", timeout=3)
        openocd_start_state = self.ocd.expect([
                "Open On-Chip Debugger[\s\S]*hardware has 6 breakpoints, 4 watchpoints",
                "Error: open failed",
                "Error: couldn't bind to socket: Address already in use"
                "init mode failed \(unable to connect to the target\)"
        ])
        if openocd_start_state == 0:
            logging.info("On-Chip debugger opened")
        elif openocd_start_state == 1:
            logging.critical("openOCD failed")
            raise OpenOCDFailed()
        elif openocd_start_state == 2:
            os.system("killall openocd")
            logging.critical("openocd already active.... Now closed, run program again")
            raise OpenOCDFailed()
        else:
            logging.critical("Unexpected problem")
            raise OpenOCDFailed()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.ocd.terminate()
        logging.info("OpenOCD terminated")

class TargetOpenOCD:
    def __init__(self, logger=logging.getLogger(__name__)):
        self.logger = logger
        logging.basicConfig(level=logging.DEBUG)
        self.ocd = pexpect.spawn("openocd -f interface/stlink-v2.cfg -f target/stm32f0x_stlink.cfg", timeout=3)
        openocd_start_state = self.ocd.expect([
                "Open On-Chip Debugger[\s\S]*hardware has 4 breakpoints, 2 watchpoints",
		"Error: open failed",
		"Error: couldn't bind to socket: Address already in use",
		"init mode failed \(unable to connect to the target\)"
	])
        if openocd_start_state == 0:
            self.logger.info("On-Chip debugger opened")
        elif openocd_start_state == 1:
            self.logger.critical("openOCD failed")
            raise OpenOCDFailed()
        elif openocd_start_state == 2:
            os.system("killall openocd")
            self.logger.critical("openocd already active.... Now closed, run program again")
            raise OpenOCDFailed()
        elif openocd_start_state == 3:
            self.logger.critical("Unable to connect to target")
            raise OpenOCDFailed()
        else:
            self.logger.critical("Unexpected problem")
            raise OpenOCDFailed()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.ocd.terminate()
        self.logger.info("OpenOCD terminated")

class TelCon:
    def __init__(self, logger = logging.getLogger(__name__)):
        self.logger = logger
        logging.basicConfig(level=logging.DEBUG)
        self.tel = pexpect.spawn("telnet localhost 4444", timeout = 3)
        telcon_start = self.tel.expect([
            "Connected to localhost",
            "unable to"
            ])
        if telcon_start == 0:
            logging.info("connected to telnet")
        else:
            raise TelConFailed()

    def __enter__(self):
        return self

    def halt(self):
        self.tel.sendline("reset halt")
        self.tel.expect("[\s\S]*target halted[\s\S]*")
        logging.info("halted")

    def remove_protection(self):
        self.tel.sendline("flash protect 0 0 last off")
        self.tel.expect("cleared protection for sectors")
        logging.info("erased")

    def erase(self):
        self.tel.sendline("flash erase_sector 0 0 0")
        self.tel.expect("[\s\S]*erased sectors[\s\S]*")
        logging.info("erased")

    def load(self, hexfile):
        self.tel.sendline("flash write_image erase "+ hexfile) # /home/pi/workspace/All/debug/DFU_ST-Link-V2.hex
        self.tel.expect("[\s\S]*wrote[\s\S]*from file[\s\S]*")
        self.tel.sendline("verify_image "+ hexfile) # /home/pi/workspace/All/debug/DFU_ST-Link-V2.hex
        self.tel.expect("[\s\S]*verified[\s\S]*bytes in[\s\S]*")
        logging.info("LOADED!")

    def __exit__(self, type, value, traceback):
        self.tel.send("exit")
        logging.info("Telnet connection terminated")

class GPIO:
    def input(pin):
        return False
    def cleanup():
        print "GPIO Cleanup"
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(4, GPIO.IN)
# GPIO.setup(17, GPIO.IN)

def flashTarget():
    try:
        with TargetOpenOCD(logger.getChild('openocd')) as openOCD:
            with TelCon(logger.getChild('telcon')) as telcon:
                telcon.halt()
                telcon.erase()
                telcon.load(target_elf)
                # light.busyOff()
                # light.success()
                # lcd.show_cursor(False)
                # lcd.blink(False)
                # lcd.clear()
                # lcd.set_cursor(6,0)
                # lcd.message("Target")
                # lcd.set_cursor(0,1)
                # lcd.message("!!!Destroyed!!!")
                # for x in range (0,20):
                #     lcd.set_backlight(1)
                #     time.sleep(0.1)
                #     lcd.set_backlight(0)
                #     time.sleep(0.1)
    except Exception:
        # lcd.show_cursor(False)
        # lcd.blink(False)
        logging.warn("Provisioning failed")
        # light.busyOff()
        # light.failed()
        # lcd.clear()
        # message = "!!Failed!!"
        # lcd.message(message)
        # lcd.set_cursor(0,1)
        # lcd.message (message)
        # for x in range(lcd_columns - len(message)):
        #     time.sleep(0.2)
        #     lcd.move_right()
        # for x in range(lcd_columns - len(message)):
        #     time.sleep(0.2)
        #     lcd.move_left()
        # lcd.clear()




while True:
    try:
        if GPIO.input(4):
            logger.info("Button pressed")
            lcd.write("Programming target")
            try:
                os.system("./target.py")
                print("=" *70)
                logger.info("Press the button")
                lcd.clear()
            except Exception:
                logger.warn("Target program not running")
                lcd.clear()
                lcd.write("Oh no!!!\nTarget Escaped")
                time.sleep(2)
                lcd.clear()
    except Exception:
        logger.warn("Main program not running")
# GPIO.cleanup()




# The real horror erupted on the day that three events happened
# simultaneously. The first event was that Breathe`o`Smart Inc. issued a
# statement to the effect that best results were achieved by using their
# systems in temperate climates.
# The second event was the breakdown of a Breathe`o`Smart system
# on a particularly hot and humid day with the resulting evacuation of
# many hundreds of office staff into the street where they met the third
# event, which was a rampaging mob of long`distance telephone
# operators who had got so twisted with having to say, all day and
# every day, "Thank you for using BS&S" to every single idiot who
# picked up a phone that they had finally taken to the streets with trash
# cans, megaphones and rifles.
# In the ensuing days of carnage every single window in the city,
# rocket`proof or not, was smashed, usually to accompanying cries of
# "Get off the line, asshole  I don't care what number you want, what
# extension you're calling from. Go and stick a firework up your bottom
# Yeeehaah  Hoo Hoo Hoo  Velooooom  Squawk " and a variety of
# other animal noises that they didn't get a chance to practise in the
# normal line of their work.
# As a result of this, all telephone operators were granted a
# constitutional right to say "Use BS&S and die " at least once an hour
# when answering the phone and all office buildings were required to
# have windows that opened, even if only a little bit.
