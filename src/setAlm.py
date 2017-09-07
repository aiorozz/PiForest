import os
import SDL_DS3231
import time
import sys

os.system("sudo rmmod rtc_ds1307")

starttime = datetime.datetime.utcnow()
ds3231 = SDL_DS3231.SDL_DS3231(1, 0x68)
#comment out the next line after the clock has been initialized
ds3231.write_now()
print "Flag", ds3231.read_flag()
ds3231.write_flag()

seg=ds3231._read_seconds()
min=ds3231._read_minutes()
hr=ds3231._read_hours()
ha=hr
mina=min

if hr<18 and hr>6:
    if min>30:
        ha=hr+1
        mina=02
    else:
        ha=hr
        mina=32
else hr>18:
    ha=06
    mina=02


ds3231.setAlm(05,mina,ha)
print "Alarma Set"




