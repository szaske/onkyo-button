#!/usr/bin/env python

# 3rd party packages
import RPi.GPIO as GPIO  # https://pypi.python.org/pypi/RPi.GPIO
import eiscp   # https://pypi.python.org/pypi/onkyo-eiscp

import time
import datetime
import logging

LedPin = 11    # pin11 --- led
BtnPin = 12    # pin12 --- button
receiver = eiscp.eISCP('192.168.1.122')  # find the receiver on the network
OnAudioVolume = '25' # Volume in hexidecimal, so this is 15/100
LowAudioVolume = '19' # Volume in hexidecimal, so this is 7/100
LengthOfLoudVolume = 248 # number of seconds to keep audio seto to loud. Longest song is 248
prev_inp = 1
count = 1
logging.basicConfig(filename=datetime.date.today().strftime("%b-%d-%Y")+".log", level=logging.INFO)
pause_time = .05 # how often the button is checked...and essentially how fast the code runs
led_blink_count = 0
led_blink_length = 25
led_state = False
vol_high = False # Volume toggle

#This sets the time the script ends each night.  Script will exit if you're trying to edit after hours :)
offhour = 21 #9pm = 21
offminute = 15 # set this to 4 as default

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

now = datetime.datetime.now()
time_to_lower = now + datetime.timedelta(seconds = LengthOfLoudVolume)


def volUp(ev=None):
        global count
        global vol_high
        global time_to_lower
        GPIO.output(LedPin, 0)  # switch led status on
        receiver.raw('MVL' + OnAudioVolume)   # Turn up audio on the Onkyo receiver
	
        # log info for each button press
	logging.info("button press #"+ str(count) + " at " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        count = count + 1 # counting button presses for logging
        vol_high = True #toggle volume

	now = datetime.datetime.now()
	time_to_lower = now + datetime.timedelta(seconds = LengthOfLoudVolume)


def volDown(ev=None):
        global count
        global vol_high

        GPIO.output(LedPin, 1)  # switch led status off
        receiver.raw('MVL' + LowAudioVolume)# Turn down audio on the Onkyo receiver
	
        # log info for each button press
	logging.info("button press #"+ str(count) + " at " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

        count = count + 1 # counting button presses for logging

        vol_high = False #toggle volume




def BtnCheck():
        global prev_inp
        global BtnPin
        global pause_time
        global blink_length
        global led_blink_count
        global led_blink_length
        global led_state
        global LedPin
        global vol_high
        #global time_to_lower

        inp = GPIO.input(BtnPin)
        
        if ((not prev_inp) and inp):    
                if (vol_high):
                        volDown()
                else:
                        volUp()
        prev_inp = inp  # This ensures that the button event is witnessed.

        if not vol_high : #if volume is low, blink lights

                # blink the LED code, to get peoples attention
                if (led_blink_count >= led_blink_length):
                        #toggle the light on
                        led_state = not led_state
                        GPIO.output(LedPin,led_state )  # switch led status on
                        led_blink_count=0
                led_blink_count += 1
        
        #pause a bit before checking the button status again.
        time.sleep(pause_time)  

        if vol_high and datetime.datetime.now()>time_to_lower: # High Volume timer, will return to blinking after x seconds
                volDown()


def killthescript():
        receiver.raw('MVL00') # set audio level to 0 before killing app
        GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource
        receiver.disconnect()           # release receiver resources

if __name__ == '__main__':     # Program start from here

	now = datetime.datetime.now()
	offTime = now.replace(hour=offhour, minute=offminute, second=0, microsecond=0)

	try:
		while datetime.datetime.now()<offTime : #Should we keep running?
                        BtnCheck() # enable button
                else:   #It's time, kill the script
                        killthescript()
                        
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		killthescript()


