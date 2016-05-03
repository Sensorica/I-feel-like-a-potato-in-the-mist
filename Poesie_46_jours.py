#!/opt/local/bin/python2.4

 #!/usr/bin/python
          # -*- coding: latin-1 -*-
import os, sys
import serial
import time
from datetime import datetime

loremFile = open ('lorem.txt')
lorem =  loremFile.read()

port = serial.Serial("/dev/tty.usbserial-A800ctKK", 115200)

time.sleep(5)

for c in lorem:
    if c == '\n':
        time.sleep(5)
        port.write(c)
        time.sleep(5)
        print (datetime.now())
    else:
        time.sleep(0.6)
        port.write(c)
        print (datetime.now())
port.close()
