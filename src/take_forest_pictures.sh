# Define a timestamp functionb
timestamp() {
  date +"%F_%T"
}

ssh -p 2222 pi@192.168.100.2 sudo python /home/pi/scripts/blink.py '2' > /dev/null

NOW=$(date +"uniandes_%Y_%m_%d_%H%M%S")
NOWNIR=$(date +"uniandes_IR_%Y_%m_%d_%H%M%S")

log_file="/home/pi/scripts/log.txt"

echo "[$(timestamp)] Taking RGB picture on forest1..."
/home/pi/scripts/take_RGB_picture.sh $NOW &
echo "[$(timestamp)] RGB picture taken!"
sleep 10
echo "[$(timestamp)] Taking NIR picture on forest2..."
command='/home/pi/scripts/take_NIR_picture.sh '
command=$command$NOWNIR
#echo $command
OUTPUT="$( ssh -p 2222 pi@192.168.100.2 $command )"
echo "[$(timestamp)] NIR picture taken!"
sleep 10
echo "[$(timestamp)] Transfering NIR picture from forest2 to forest1..."
scp -P 2222 pi@192.168.100.2:/home/pi/forest-pictures/${OUTPUT} /home/pi/forest-pictures
echo "[$(timestamp)] NIR picture transfered!"

#echo "[$(timestamp)] Deleting NIR picture on forest2..."
ssh -p 2222 pi@192.168.100.2 rm /home/pi/forest-pictures/${OUTPUT}
echo "[$(timestamp)] NIR picture deleted!"

ssh -p 2222 pi@192.168.100.2 sudo python /home/pi/scripts/blink.py '3' > /dev/null
