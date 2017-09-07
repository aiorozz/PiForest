import RPi.GPIO as GPIO
import time
import sys

num1=sys.argv[1]
#print(num1)
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

if num1=='1':
   GPIO.output(17,False)
   GPIO.output(27,True)
   #time.sleep(10)
elif num1=='2':
   GPIO.output(17,True)
   GPIO.output(27,False)
elif num1=='3':
   GPIO.output(17,True)
   GPIO.output(27,True)
else:
   GPIO.output(17,False)
   GPIO.output(27,False)
   #time.sleep(10)
#GPIO.cleanup()	

