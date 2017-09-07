import os
import re
import time
import serial

os.system("ssh -p 2222 pi@192.168.100.2 sudo python /home/pi/scripts/blink.py '1' > /dev/null")
date_time_regex = re.compile('(\d{4})-(\d{1,3})-(\d{1,3}) (\d{1,3}):(\d{1,3}):(\d{1,3})')

try:
    datet=datetime.datetime.now()
    response=-1
    while responde !=0:
        while not regex_Ok:
            if date_time_regex.match(datet):
                regex_OK = True
                print("Fecha establecida")
            else:
                regex_OK = False
                print("Fecha no establecida")

    date_time_cmd = "'" + datet + "'"
    command = "sudo date -s %s > /dev/null" % (date_time_cmd)
    os.system("echo 'Setting forest1 system time...' >> /home/pi/scripts/log.txt")
    response = os.system(command)
    command = "ssh -p 2222 pi@192.168.100.2 /home/pi/scripts/set_date_time.sh %s > /dev/null" % (date_time_cmd)
    os.system("echo 'Setting forest2 system time...' >> /home/pi/scripts/log.txt")
    response = os.system(command)
    response=0
    os.system("ssh -p 2222 pi@192.168.100.2 sudo python /home/pi/scripts/blink.py '2' > /dev/null")
    time.sleep(1)
except serial.serialutil.SerialException:
    pass
