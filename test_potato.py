#!/opt/local/bin/python2.4

 #!/usr/bin/python
          # -*- coding: latin-1 -*-
import os, sys
import serial
import time
from datetime import datetime

#port = serial.Serial("/dev/tty.usbserial-A800ctKK", 115200)

loremFile = open ('lorem.txt')
lorem =  loremFile.read()
loremLength = len(lorem)
print loremLength
maxLength = 50
loremIndex = 0

while loremIndex <= loremLength:
    lineLength = maxLength
    
    while lorem[loremIndex + lineLength] != " ":
	    lineLength -= 1
    
    printLine = lorem [loremIndex:loremIndex + lineLength] + '\n'	
    print printLine
    print len(printLine)
    print lineLength
    for c in printLine:
        if c == '\n':
            time.sleep(5)
            #port.write(c)
            print "new line"
            time.sleep(5)
        else:
            time.sleep(0.6)
            #port.write(c)
            print c
    loremIndex += lineLength
#port.close()