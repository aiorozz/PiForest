import os
import time
import subprocess

count=0
while (count<120): 
	comand_run=subprocess.call("sudo mount" + " /dev/sda1" + " /media/usb",shell=True)
	#comand_run2=subprocess.call("sudo fdisk -l",shell=True)
	if comand_run==0:
	 os.system("sudo mkdir /mnt/usb")
	 os.system("sudo cp -r /home/pi/forest-pictures/ /media/usb")
         os.system("sudo rm /home/pi/forest-pictures/* ")
	 os.system("sudo umount /media/usb ")
	 time.sleep(5)
	 count=160	
	else:
 	 time.sleep(5)
 	 pass
	count=count+1
	print (count)

