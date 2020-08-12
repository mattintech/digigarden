#!/usr/bin/env python3

import requests
from digiGarden import dbHelper
    

def getSolarData():
    r = requests.get('http://localhost:5000/api/solar')
    ## Get status code
    r.status_code
    ## get body in a dict
    jsonResponse = r.json()
    dbHelper.addSolarData(
        (
        jsonResponse['batteryVoltage'],
        jsonResponse['solarVoltage'],
        jsonResponse['chargingCurrent'],
        jsonResponse['loadCurrent'])
        )

def getPiData():
    r = requests.get('http://localhost:5000/api/piData')
    ## Get status code
    r.status_code
    ## get body in a dict
    jsonResponse = r.json()
    dbHelper.piStatistics(
        (
        jsonResponse['hostname'],
        jsonResponse['wlan_ipaddress'],
        jsonResponse['free_space'],
        jsonResponse['pi_temperature'])
        )



getSolarData()
getPiData()