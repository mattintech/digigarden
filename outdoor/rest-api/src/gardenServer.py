#!/usr/bin/python
import random
import socket
from flask import Flask, jsonify

hostname=socket.gethostname()

apiWebServerPort=5000
app = Flask(__name__)

## to populate fake data to the API for testing
def getRandNumber():
    return random.randint(1,30)

##AppRoutes - basic test to make sure its working
@app.route('/', methods=['GET'])
def home():
    return 'Welcome to the Garden API Server!  Docker host: '+ hostname

## route to display data from serial controller
@app.route('/api/solar', methods=['GET'])
def getSolarData():
    try:
         return jsonify(
                            batteryVoltage=getRandNumber(),
                            solarVoltage=getRandNumber(),
                            chargingCurrent=getRandNumber(),
                            loadCurrent=getRandNumber())

    #except (IndexError, IOError) as e:
    except Exception as e:
        print(e)
        #return jsonify({'error': e.message}), 503

try: 
    app.run(host='0.0.0.0', port=apiWebServerPort)
    print("Starting API Server...")
except KeyboardInterrupt:
    print("Ctrl-C pressed.  Exiting. ")
    
