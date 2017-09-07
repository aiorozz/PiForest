#!/usr/bin/env python
#
# Test SDL_DS3231
# John C. Shovic, SwitchDoc Labs
# 08/03/2014
#
#

# imports

import sys
import time
import datetime
import SDL_DS3231

# Main Program

print ""
print "Test SDL_DS3231 Version 1.0 - SwitchDoc Labs"
print ""
print ""
print "Program Started at:"+ time.strftime("%Y-%m-%d %H:%M:%S")
print ""

filename = time.strftime("%Y-%m-%d%H:%M:%SRTCTest") + ".txt"
starttime = datetime.datetime.utcnow()

ds3231 = SDL_DS3231.SDL_DS3231(1, 0x68)
#comment out the next line after the clock has been initialized
ds3231.write_now()
count=0

while (count<2):

	#
	currenttime = datetime.datetime.utcnow()
	print ""
	print "Raspberry Pi=\t" + time.strftime("%Y-%m-%d %H:%M:%S")
	
	print "DS3231=\t\t%s" % ds3231.read_datetime()
 	ds3231.setAlm(05,35,18)
    	print "Alarma Set"
	print "Control", ds3231.read_control()
	print "Alm min", ds3231.read_almmin()
	print "Flag", ds3231.read_flag()
	print "DS3231 Temp=", ds3231.getTemp()
	count= count+1
	time.sleep(10.0)
