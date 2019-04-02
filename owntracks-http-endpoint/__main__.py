#!/usr/bin/env python3
from flask import Flask, request
from helper.location import Location
import json

# debug
debug = True
from datetime import datetime
from debug.randomGeoCoordinates import GeoCoor

application = Flask(__name__)

# this is called if a device submits a new position
# stores new position in database and delivers the last reported position of all friends of this device
@application.route('/pub', methods = ['POST'])
def addNewDatapoint():
    datapoint = request.data
    if debug:
        f = open("locations.txt","a+")
        f.write(str(datapoint) + "\n")
    parsedDatapoint = json.loads(datapoint.decode("utf-8"))
    if parsedDatapoint["_type"] == 'location':
        # store information from given datapoint
        location = Location()
        location.accuracy = parsedDatapoint["acc"]
        location.altitude = parsedDatapoint["alt"]
        location.battery = parsedDatapoint["batt"]
        location.connection = parsedDatapoint["conn"]
        location.latitude = parsedDatapoint["lat"]
        location.longitude = parsedDatapoint["lon"]
        # catch if trigger is transmitted (Move mode)
        try:
            location.trigger = parsedDatapoint["t"]
        except KeyError as e:
            location.trigger = "UNDEFINED"
        location.trackerID = parsedDatapoint["tid"]
        location.timestamp = parsedDatapoint["tst"]
        location.velocity = parsedDatapoint["vel"]

        if debug:
            f = open("locations.txt","a+")
            f.write("Acc: " + str(location.accuracy) +
                    " Alt: " + str(location.altitude) +
                    " Batt: " + str(location.battery) + 
                    " Conn: " + str(location.connection) +
                    " Lat: " + str(location.latitude) + 
                    " Lon: " + str(location.longitude) + 
                    " T: " + str(location.trigger) +
                    " TID: " + str(location.trackerID) + 
                    " Tst: " + str(location.timestamp) + 
                    " Vel: " + str(location.velocity) + "\n")

        return '{"_type":"location","acc":16,"alt":0,"batt":4,"conn":"w","lat":' + GeoCoor.randomCoordsLat() + ',"lon":' + GeoCoor.randomCoordsLon() + ',"t":"u","tid":"wo","tst":' + str(int(datetime.timestamp(datetime.now())) - 300) + ',"vac":0,"vel":0}'
    else:
        f = open("locations.txt","a+")
        f.write(json.dumps(datapoint.decode("utf-8")) + "\n")
        return ''

if __name__ == '__main__':
    application.run(debug = True, host='0.0.0.0')