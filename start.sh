#!/bin/sh
while true
do
    /usr/bin/python3 /home/pi/led-demo/sign.py
    /home/pi/rpi-rgb-led-matrix/examples-api-use/demo -D0 --led-chain=4 --led-parallel=2 --led-slowdown-gpio=2 -t30
    /usr/bin/python3 /home/pi/led-demo/clock.py --led-chain=4 --led-parallel=2 --led-slowdown-gpio=2
done
