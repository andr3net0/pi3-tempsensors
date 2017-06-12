#!/usr/bin/python
# Copyright (c) 2017 Logicc Systems Ltd.
# 
# Bases on AdafruitDHT - thanks guys!

import sys
import Adafruit_DHT
import settings
from time import sleep

try:
    verbose = settings.VERBOSE
    DHT_V = settings.DHT_V
    serial = settings.PI_KEY
except Exception, e:
    print __name__ + ": Could not read settings"
    print e
    sys.exit(1)

try:
    DHT_PINS = settings.DHT_PINS
except:
    if verbose:
        print 'set DHT_PINS = []'
    DHT_PINS = []



# Try to grab a sensor reading.
def readDHT():
    values=[]
    for i, pin in enumerate(DHT_PINS):
        for num in range(1,5):
            humidity, temperature = Adafruit_DHT.read(DHT_V, pin)
            if humidity is not None and temperature is not None and humidity < 120:
                if verbose:
                    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
                break
            sleep(2) 
        if humidity > 120:
            humidity, temperature = None, None
        values.append(('H-'+str(pin)+'@'+str(serial),humidity,'humidity'))
        values.append(('T-'+str(pin)+'@'+str(serial),temperature,'temperature'))
        
    return values


