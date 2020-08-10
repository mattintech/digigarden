#!/usr/bin/python

import requests

r = requests.get('http://127.0.0.1:5000/api/solar')

## Get status code
r.status_code

## get body
print(r.text)

