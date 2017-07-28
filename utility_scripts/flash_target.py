# This is a stripped down version of the code that runs on the pi, used for
# testing and development.
import pexpect
import logging
import os

elf_file = "/home/jonathan/stm_jig/binaries/demo_2015.elf"




class TelConFailed(Exception):
    pass

class TelCon:
    def __init__(self, logger=logging.getLogger(__name__)):
        self.logger = logger
        logging.basicConfig(level=logging.DEBUG)
        self.tel = pexpect.spawn("telnet localhost 4444", timeout = 3)
        telcon_start = self.tel.expect([
            "Connected to localhost",
            "unable to"
        ])
        if telcon_start == 0:
            self.logger.info("connected to telnet")
        else:
            raise TelConFailed()

    def __enter__(self):
        return self

    def halt(self):
        self.tel.sendline("reset halt")
        self.tel.expect_exact("target halted")
        self.logger.info("halted")

    def erase(self):
        self.tel.sendline("flash erase_sector 0 0 0")
        self.tel.expect_exact("erased sectors")
        self.logger.info("erased")

    def load(self):
        self.tel.sendline("flash write_image erase "+elf_file)
        self.tel.expect("wrote [\s\S]* from file")
        self.tel.sendline("verify_image "+elf_file)
        self.tel.expect("verified[\s\S]*bytes in")
        self.logger.info("Loaded and verified")

    def __exit__(self, type, value, traceback):
        self.tel.terminate()
        self.logger.info("Telnet connection terminated")

class OpenOCDFailed(Exception):
    pass

class OpenOCD:
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



logging.basicConfig(format = "%(asctime)s:" + logging.BASIC_FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


try:
    with OpenOCD(logger.getChild('openocd')) as openOCD:
        with TelCon(logger.getChild('telcon')) as telcon:
            telcon.halt()
            telcon.erase()
            telcon.load()
            print "success? :)"

except Exception:
    logging.warn("Provisioning failed")
