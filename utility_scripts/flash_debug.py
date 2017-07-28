# This is a stripped down version of the code that runs on the pi, used for
# testing and development.
import pexpect
import logging
import os

dfu_hex = '/home/jonathan/stm_jig/binaries/DFU_ST-Link-V2.hex'



class TelConFailed(Exception):
    pass

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

    def load(self):
        self.tel.sendline("flash write_image erase "+dfu_hex)
        self.tel.expect("[\s\S]*wrote[\s\S]*from file[\s\S]*")
        self.tel.sendline("verify_image "+dfu_hex)
        self.tel.expect("[\s\S]*verified[\s\S]*bytes in[\s\S]*")
        logging.info("LOADED!")

    def __exit__(self, type, value, traceback):
        self.tel.send("exit")
        logging.info("Telnet connection terminated")

class OpenOCDFailed(Exception):
    pass

class OpenOCD:
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


logging.basicConfig(format = "%(asctime)s:" + logging.BASIC_FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


try:
    with OpenOCD(logger.getChild('openocd')) as openOCD:
        with TelCon(logger.getChild('telcon')) as telcon:
            telcon.halt()
            telcon.remove_protection()
            telcon.halt()
            telcon.erase()
            telcon.load()
            print "success? :)"

except Exception:
    logging.warn("Provisioning failed")
