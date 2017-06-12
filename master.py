#!/usr/bin/python
# Copyright (c) 2017 Logicc Systems Ltd.
# Author: Andre Neto

import sys
import datetime

try:
    import getAdc
    import getTemps
    import getSwitches
    import getHumidity
    import putDataDB
    import putDataAPI
    import settings
    import setWarning
except  Exception, e:
    print e
    print "Main: Could not perform import"
    sys.exit(1)

try:
    serial = settings.PI_KEY
    APIPOST = settings.APIPOST
    verbose = settings.VERBOSE
    tempwarn = settings.TEMPWARN
except Exception, e:
    "Main: Could not read settings"
    print e
    sys.exit(1)

data = []

print "Begin master.py"
print datetime.datetime.now().strftime('%Y-%m-%d')
print datetime.datetime.now().strftime('%H:%M:%S')
print '\tRead CTs - ADC_CHANNELS'
ctData = getAdc.readCT()
if verbose:
    print ctData
data.extend(ctData)

print datetime.datetime.now().strftime('%H:%M:%S')
print '\tRead Temps - OneWire'
temps = getTemps.readProbes()
if verbose:
    print temps
data.extend(temps)

print datetime.datetime.now().strftime('%H:%M:%S')
print '\tRead Switches - DOOR_PINS'
switches = getSwitches.readSwitches()
if verbose:
    print switches
data.extend(switches)

print datetime.datetime.now().strftime('%H:%M:%S')
print '\tRead DHT - DHT_PINS'
dhts = getHumidity.readDHT()
if verbose:
    print dhts
data.extend(dhts)

print datetime.datetime.now().strftime('%H:%M:%S')
print '\tsave to DB'
putDataDB.postData(data)

print datetime.datetime.now().strftime('%H:%M:%S')

if APIPOST:
    print '\tpost to API'
    putDataAPI.postDBData()
    print datetime.datetime.now().strftime('%H:%M:%S')

if APIPOST:
    temp = int(datetime.datetime.now().strftime('%H%M'))
    if temp < 10:
        print '\tclean old Data from DB'
        putDataDB.cleanData()
        print datetime.datetime.now().strftime('%H:%M:%S')

if tempwarn:
    print '\tset Warning'
    setWarning.setWarn(data)
    print datetime.datetime.now().strftime('%H:%M:%S')

print "End master.py"
print

