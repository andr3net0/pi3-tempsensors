#!/usr/bin/python
# Copyright (c) 2017 Logicc Systems Ltd.
# Author: Andre Neto
# Bases on script by Alex Eames http://RasPi.tv  
# http://raspi.tv/?p=6791  
  
import RPi.GPIO as GPIO  
import settings
import sys
from time import sleep
import pickle

try:
    verbose = settings.VERBOSE
    serial = settings.PI_KEY
except Exception, e:
    print __name__ + ": Could not read settings"
    print e
    sys.exit(1)

try:
    WARN_PIN = settings.WARN_PIN
except:
    if verbose:
        print 'set WARN_PIN = None'
    WARN_PIN = None

try:
    SIGNAL_TIME = settings.SIGNAL_TIME
except:
    if verbose:
        print 'set SIGNAL_TIME = 5'
    SIGNAL_TIME = 5


GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
if WARN_PIN is not None:
    GPIO.setup(WARN_PIN, GPIO.OUT, initial=GPIO.LOW)    # set pin (GPIO.BCM number) as input (button)  

def setWarn( data ):
    try:
        f = open('limits.pckl', 'rb')
        limits = pickle.load(f)
        f.close()
        if verbose:
            print 'configured limits'
            print limits
    except:
        limits = None

    for item in data:
        if item[2] == 'temperature':
            if verbose:
                print 'temperature item:'
                print item
            try:
                limit = limits[item[0]]
                print limit
            except:
                limit = None
            if limit is not None and (item[1] > limit['max'] or item[1] < limit['min']):
                if verbose:
                    print 'setting warning'
                GPIO.output(WARN_PIN, GPIO.HIGH)
                sleep(SIGNAL_TIME)
                if verbose:
                    print 'clearing warning'
                GPIO.output(WARN_PIN, GPIO.LOW)
                return True
    return False
