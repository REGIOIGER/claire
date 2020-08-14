#!/usr/bin/env python

from gps import *
import time

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

f = open("/home/ubuntu/data.csv","w")


def talker():
    strdata = ""
    
    while True:
        nx = gpsd.next()
        if nx['class'] == 'TPV':
            latitude = getattr(nx,'lat', "Unknown")
            longitude = getattr(nx,'lon', "Unknown")
            strdata = str(latitude) + ", " + str(longitude)
        f.write(strdata)
        f.write("\n")
        time.sleep(0.200)

if __name__ == '__main__':
    try:
        talker()
    except KeyboardInterrupt:
        fclose()
        pass
