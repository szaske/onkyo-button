#!/usr/bin/env python
import RPi.GPIO as GPIO  # https://pypi.python.org/pypi/RPi.GPIO
import eiscp  # https://pypi.python.org/pypi/onkyo-eiscp
import psutil  # https://pypi.python.org/pypi/psutil/

procname = "python"

LedPin = 11    # pin11 --- led
BtnPin = 12    # pin12 --- button
receiver = eiscp.eISCP('192.168.1.122')  # find the receiver on the network
GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def killthescript():
    receiver.raw('MVL00') # set audio level to 0 before killing app
    GPIO.output(LedPin, GPIO.HIGH)     # led off
    GPIO.cleanup()                     # Release resource
    receiver.disconnect()           # release receiver resources

for proc in psutil.process_iter():
    # check whether the process name matches
    if proc.name() == procname:
        proc.kill()

killthescript()


