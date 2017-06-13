#!/usr/bin/python
# Copyright (c) 2017 Logicc Systems Ltd.
# Author: Andre Neto
  
import time
import subprocess
import os
import requests
import settings
import sqlite3
import sys
import json
import pickle

try:
    url = settings.URL_LIMTS
    api_key = settings.API_KEY
    verbose = settings.VERBOSE
    pi_key = settings.PI_KEY
except:
    print "Could not read settings"
    sys.exit(1)



def getFromUrl(key):
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    api_call = url + '?key=' + api_key + '&boardid=' + pi_key
    try:
        response = requests.request("GET", api_call)
    except Exception, e:
        print e
        print __name__ + ": error on url call"
        return response.request 
    
    # Show additional info for troubleshooting
    if verbose:
        print "Called : " + str(api_call)
        print "Response - " + str(response.status_code)
        print response.text

    if response.status_code == 200:
        limitsJson = response.text
        
    else:
        return response.status_code
    
    try:
        limits = json.loads(limitsJson)
    except Exception, e:
        print e
        print __name__ + ": error decoding response"
        return 

    f = open('limits.pckl', 'wb')
    pickle.dump(limits, f)
    f.close()

    return response.status_code


getFromUrl(api_key)
