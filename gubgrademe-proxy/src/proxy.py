from flask import Flask
from flask import request
from flask import Response
import json
import requests

app = Flask(__name__)


@app.route('/')
def proxy():
    # Service requested by the frontend
    serviceCalled = request.args.get('service')

    # Modules sent with service request
    reqmod1 = request.args.get('module_1')
    reqmod2 = request.args.get('module_2')
    reqmod3 = request.args.get('module_3')
    reqmod4 = request.args.get('module_4')
    reqmod5 = request.args.get('module_5')

    # Marks sent with service request
    reqmark1 = request.args.get('mark_1')
    reqmark2 = request.args.get('mark_2')
    reqmark3 = request.args.get('mark_3')
    reqmark4 = request.args.get('mark_4')
    reqmark5 = request.args.get('mark_5')

    # Paramters to be relayed to the service
    parameters = {"module_1": reqmod1, "module_2": reqmod2, "module_3": reqmod3, "module_4": reqmod4, "module_5": reqmod5,
                  "mark_1": reqmark1, "mark_2": reqmark2, "mark_3": reqmark3, "mark_4": reqmark4, "mark_5": reqmark5}

    # F. Stateful Saving of Current Values
    requsername = request.args.get('username')    
    reqtypeOfRequest = request.args.get('typeOfRequest')

    reqsort = request.args.get('sort')
    reqmaxmin = request.args.get('maxmin')
    reqtotal = request.args.get('total')
    reqclassify = request.args.get('classify')
    reqaverage = request.args.get('average') 
    reqmedian = request.args.get('median')
    
    if serviceCalled == 'database':
        parameters = {"typeOfRequest": reqtypeOfRequest, "username": requsername, "sort": reqsort, "maxmin": reqmaxmin, "total": reqtotal , "classify": reqclassify,"average": reqaverage, "median": reqmedian, "module_1": reqmod1, "module_2": reqmod2, "module_3": reqmod3, "module_4": reqmod4, "module_5": reqmod5,
                  "mark_1": reqmark1, "mark_2": reqmark2, "mark_3": reqmark3, "mark_4": reqmark4, "mark_5": reqmark5}

    # Importing the config file with the urls
    serviceFile = open("service-config.json", "r")
    serviceFileJson = serviceFile.read()
    services = json.loads(serviceFileJson)

    # Check the requested service against the service config file
    for service in services:
        if service['service'] == serviceCalled:
            # Relay the reuqest to the matching service
            proxyrequest = requests.get(
                url=service['serviceURL'], params=parameters)
            responseToFrontend = Response(
                response=proxyrequest, status=200, mimetype='application/json')
            responseToFrontend.headers["Content-Type"] = "application/json"
            responseToFrontend.headers["Access-Control-Allow-Origin"] = "*"
            return responseToFrontend

    # If the requested service is not found - return a 400 error
    serviceNotFound = {"error": True,
                       "errormessage": "Requested service does not exist", "result": None}
    reply = json.dumps(serviceNotFound)
    responseToFrontend = Response(
        response=reply, status=400, mimetype='application/json')
    responseToFrontend.headers["Content-Type"] = "application/json"
    responseToFrontend.headers["Access-Control-Allow-Origin"] = "*"
    return responseToFrontend


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# ?service=maxmin&module_1=m1&mark_1=50&module_2=m2&mark_2=90&module_3=m3&mark_3=80&module_4=m4&mark_4=60&module_5=m5&mark_5=70
