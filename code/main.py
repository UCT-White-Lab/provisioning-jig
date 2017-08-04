# Going to thrown everything in this one file for now, and then split it back out
# as I add in IO, LCD, logging etc.
import logging, time, pexpect, os, usb.core

wd = os.path.dirname(os.path.realpath(__file__))

target_elf = wd + '/../binaries/main.elf' #<<<<<<<<<<<<<<<<<
debug_hex = wd + "/../binaries/DFU_ST-Link-V2.hex"

pNum = 2 # Which USB PORT IS POWERS THE DEBUGGERS?

logging.basicConfig(format = "%(asctime)s:" + logging.BASIC_FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class LCD:
    def write(self, str):
        print "Lcd: " + str
    def clear(self):
        print "Lcd clear"

lcd = LCD()

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
        logging.info("removed protection")

    def erase(self):
        self.tel.sendline("flash erase_sector 0 0 0")
        self.tel.expect("[\s\S]*erased sectors[\s\S]*")
        logging.info("erased")

    def load(self, hexfile):
        self.tel.sendline("flash write_image erase "+ hexfile) # /home/pi/workspace/All/debug/DFU_ST-Link-V2.hex
        self.tel.expect("[\s\S]*wrote[\s\S]*from file[\s\S]*")
        logging.info("Loaded")
        self.tel.sendline("verify_image "+ hexfile) # /home/pi/workspace/All/debug/DFU_ST-Link-V2.hex
        self.tel.expect("[\s\S]*verified[\s\S]*bytes in[\s\S]*")
        logging.info("Verified")

    def __exit__(self, type, value, traceback):
        self.tel.send("exit")
        logging.info("Telnet connection terminated")

class GPIO:
    def input(pin):
        return False
    def cleanup():
        print "GPIO Cleanup"

class LEDS:
    green_leds = []
    # Pin stuff for WS2812 setup etc here <<<
    def lightPin(self, pinNum, fail=False):
        if fail:
            print "LED %i RED" % pinNum
        else:
            print "LED %i GREEN" % pinNum
            self.green_leds.append(pinNum)

    def redPins(self):
        if len(self.green_leds) != 0:
            print "Turning pins from %i onward RED" % self.green_leds[len(self.green_leds)-1]

led = LEDS() # Not sure this is the best way to do this, but makes for easy testing

def powerOff():
    print "USB POWER OFF"
    hubs = usb.core.find(find_all=True, bDeviceClass=usb.CLASS_HUB)
	dev_hub = hubs.next()
	dev_hub.ctrl_transfer((usb.TYPE_CLASS | usb.RECIP_OTHER), 1, 8, pNum)

def powerOn():
    print "USB POWER ON"
    hubs = usb.core.find(find_all=True, bDeviceClass=usb.CLASS_HUB)
    dev_hub = hubs.next()
    dev_hub.ctrl_transfer((usb.TYPE_CLASS | usb.RECIP_OTHER), 3, 8, pNum)

def toggleUSBPower():
    print "Toggling USB POWER"
    powerOff()
    time.sleep(0.1)
    powerOn()


def flashTarget():
    try:
        with TargetOpenOCD(logger.getChild('openocd')) as openOCD:
            lcd.write("Started OpenOCD")
            led.lightPin(1)
            with TelCon(logger.getChild('telcon')) as telcon:
                led.lightPin(3)
                lcd.write("Established \nConnection")
                telcon.halt()
                led.lightPin(5)
                lcd.write("Halted target")
                telcon.erase()
                led.lightPin(7)
                lcd.write("Erased target")
                telcon.load(target_elf)
                led.lightPin(9)
                led.lightPin(11)
                lcd.write("Loaded demo elf\n Finished!!")
            led.lightPin(13)
        led.lightPin(15)
    except Exception:
        logging.warn("Target provisioning failed")

def flashDebug():
    try:
        toggleUSBPower()
        led.lightPin(1)
        time.sleep(0.1)
        try:
            with DebugOpenOCD(logger.getChild('openocd')) as openOCD:
                led.lightPin(2)
                with TelCon(logger.getChild('telcon')) as telcon:
                    led.lightPin(3)
                    telcon.halt()
                    led.lightPin(4)
                    telcon.remove_protection()
                    led.lightPin(5)
                    telcon.halt()
                    led.lightPin(6)
                    telcon.erase()
                    led.lightPin(7)
                    telcon.load(debug_hex)
                    led.lightPin(8)
                    led.lightPin(9)
                led.lightPin(10)
            led.lightPin(11)
        except:
            logging.warn("Provisioning failed")
        toggleUSBPower()
        led.lightPin(12)
        print "Update fw here" # Hard stuff to come

    except Exception:
        logging.warn("Lights or button initialisation failed")



button_target = False
button_debug = True

logger.info("Button pressed")
if button_target:
    lcd.write("Target Selected")
    logger.info("Target Selected")
    try:
        flashTarget()
        led.lightPin(17)
        led.lightPin(18)
    except Exception:
        led.redPins() # turns all remaining LEDs red
        logger.warn("Target flashing failed")
        lcd.clear()
        lcd.write("Oh no!!!\nTarget Escaped")
        time.sleep(2)
        lcd.clear()
# GPIO.cleanup()

elif button_debug:
    lcd.write("Programming Debugger")
    logger.info("Debugger Selected")
    try:
        flashDebug()
    except Exception:
        logger.warn("Programming debugger failed")
        lcd.clear()
        lcd.write("Oh no!!!\nDebugger not flashed")
        time.sleep(2)
        lcd.clear()


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
