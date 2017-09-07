import RPi.GPIO as GPIO
import time
import os
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.OUT, initial=GPIO.DOWN)
fin=0
while fin=1:
    if (GPIO.input(19) == '0'):
        GPIO.output(26,True)
        time.sleep(1)
        GPIO.output(26,False)
        fin=0
    else:
        GPIO.output(26,False)

os.system("sudo reboot")
