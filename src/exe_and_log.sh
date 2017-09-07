echo "***Starting***"  >> /home/pi/scripts/log.txt

echo "1 - Waiting till Forest2 is up..." >> /home/pi/scripts/log.txt
/home/pi/scripts/wait_4_host_up_2.sh 192.168.100.2 >> /home/pi/scripts/log.txt

echo "2 - Setting time Forest..." >> /home/pi/scripts/log.txt
/home/pi/scripts/setTime.sh  >> /home/pi/scripts/log.txt

echo "3 - Taking pictures..." >> /home/pi/scripts/log.txt
/home/pi/scripts/take_forest_pictures.sh >> /home/pi/scripts/log.txt

echo "4 - Waiting 10 minutes to halt and copy..." >> /home/pi/scripts/log.txt
python /home/pi/scripts/copyimg.py

#echo "4 - Waiting till stephanie is down..." >> /home/pi/scripts/log.txt
#/home/pi/scripts/wait_4_host_down_2.sh 192.168.100.3 >> /home/pi/scripts/log.txt

#echo "5 - Shutting down system..." >> /home/pi/scripts/log.txt
#/home/pi/scripts/shutdown_system.sh >> /home/pi/scripts/log.txt

echo "END" >> /home/pi/scripts/log.txt
