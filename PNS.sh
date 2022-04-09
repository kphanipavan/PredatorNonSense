#!/bin/bash
#echo 'For Jade Predator Helios 300 PH315-53-72W3'
#nohup sudo python3 main.py > output.log &

echo 'For Jade Predator Helios 300 PH315-53-72W3'
sudo nohup bash -c "python3 main.py > output.log && cd /home/plant/Git/PredatorNonSense/ && nohup evtest /dev/input/event4 | stdbuf -o0 grep -m 1 'code 425 (KEY_PRESENTATION), value 1' && /home/plant/Git/PredatorNonSense/PNS.sh &"
