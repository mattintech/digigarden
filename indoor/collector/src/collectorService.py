#!/usr/bin/env python3

import requests
from digiGarden import dbHelper

r = requests.get('http://localhost:5000/api/solar')

## Get status code
r.status_code

## get body
print(r.text)
jsonResponse = r.json()

print(jsonResponse['charingCurrent'])

dbHelper.addSolarData((
    jsonResponse['batteryVoltage'],
    jsonResponse['solarVoltage'],
    jsonResponse['charingCurrent'],
    jsonResponse['loadCurrent'])
)
