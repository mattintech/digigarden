#!/usr/bin/python
import random
from flask import Flask, jsonify
from digiGardenServer import piDataUtils

apiWebServerPort=5000
app = Flask(__name__)

## to populate fake data to the API for testing
def getRandNumber():
    return random.randint(1,30)

##AppRoutes - basic test to make sure its working
@app.route('/', methods=['GET'])
def home():
    return 'Welcome to the Garden API Server!  Docker host: '+ deviceHostname

## route to display data from serial controller
@app.route('/api/solar', methods=['GET'])
def getSolarData():
    try:
         return jsonify(
                            batteryVoltage=getRandNumber(),
                            solarVoltage=getRandNumber(),
                            chargingCurrent=getRandNumber(),
                            loadCurrent=getRandNumber())
    except (IndexError, IOError) as e:
        return jsonify({'error': e.message}), 503

## Pi Stats
@app.route('/api/piData', methods=['GET'])
def getPiData():
    try:
        return jsonify(
                hostname=piDataUtils.hostname,
                wlan_ipaddress=piDataUtils.ipaddr,
                free_space=piDataUtils.getFreeSpaceInMb()
        )
    except (IndexError, IOError) as e:
        return jsonify({'error': e.message}), 503

try: 
    app.run(host='0.0.0.0', port=apiWebServerPort)
    print("Starting API Server...")
except KeyboardInterrupt:
    print("Ctrl-C pressed.  Exiting. ")
    
