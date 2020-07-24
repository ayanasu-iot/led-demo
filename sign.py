#!/usr/bin/env python3
import subprocess


if __name__ == "__main__":
    out = "舞鶴高専電気情報工学科へようこそ!! Welcome to NIT. Maizuru College, Department of Electrical & Computer Engineering!!"
    subprocess.call('sudo convert -background black -fill "#9057FF" -font /usr/local/share/fonts/A-OTF-ShinGoPro-Regular.otf -pointsize 30 label:"{0}" /home/pi/led-demo/sign.png'.format(out),shell=True)
    subprocess.call('sudo python3 image-scroller.py --led-chain=4 --led-parallel=2 -i /home/pi/led-demo/sign.png -b 80 --led-slowdown-gpio=2',shell=True)
