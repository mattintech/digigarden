#!/usr/bin/env python3

import requests

r = requests.get('http://localhost:5000/api/solar')

## Get status code
r.status_code

## get body
print(r.text)
jsonResponse = r.json()

print(jsonResponse['chargingCurrent'])
