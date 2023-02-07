import serial
import re

'''
Manages a singular USB GPIB device. Implements sending and receiving of commands with basic error checking.
Requires a port adress on initialization.
'''
class USBGPIB:

    def __init__(self, usb_address):
        self.ser = serial.Serial(usb_address, 115200, timeout = 0.2)

    def is_common(self, cmd)
        return bool(re.match(r"^\*[a-zA-Z]{3}\??(?: [1-9E+\.]{1,})?$", cmd))
        

    def common_cmd(self, cmd):
        assert self.is_common(cmd)
        self.ser.write(cmd + "\n")
    
    def cmd(self, cmd):
        assert bool(re.match(r"^[a-zA-Z]{3}\?? ?", cmd))
        self.ser.write(cmd + "\n")

    def query(self, cmd):
        if self.is_common(cmd):
            self.common_cmd(cmd);
        else:
            self.cmd(cmd)
        
        # then read until we get a newline