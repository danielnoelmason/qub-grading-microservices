import logging

import azure.functions as func

import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    rmark1 = req.params.get('mark_1')
    rmark2 = req.params.get('mark_2')
    rmark3 = req.params.get('mark_3')
    rmark4 = req.params.get('mark_4')
    rmark5 = req.params.get('mark_5')

#missing parameter error
    if not rmark1:
        responseJSON = {
            "error": True,
            "errormessage": "Mark 1 was not provided",
            "output": None
        }
        response = json.dumps(responseJSON)
        return func.HttpResponse(response)
    
    if not rmark2:
        responseJSON = {
            "error": True,
            "errormessage": "Mark 2 was not provided",
            "output": None
        }
        response = json.dumps(responseJSON)
        return func.HttpResponse(response)
    if not rmark3:
        responseJSON = {
            "error": True,
            "errormessage": "Mark 3 was not provided",
            "output": None
        }
        response = json.dumps(responseJSON)
        return func.HttpResponse(response)
    if not rmark4:
        responseJSON = {
            "error": True,
            "errormessage": "Mark 4 was not provided",
            "output": None
        }
        response = json.dumps(responseJSON)
        return func.HttpResponse(response)
    if not rmark5:
        responseJSON = {
            "error": True,
            "errormessage": "Mark 5 was not provided",
            "output": None
        }
        response = json.dumps(responseJSON)
        return func.HttpResponse(response)
    
#string conversion error
    try:
        mark_1 = int(rmark1)
        mark_2 = int(rmark2)
        mark_3 = int(rmark3)
        mark_4 = int(rmark4)
        mark_5 = int(rmark5)
    except ValueError:
        responseJSON = {
            "error": True,
            "errormessage": "Invalid mark provided (must be int)",
            "output": None
        }
        response = json.dumps(responseJSON)
        return func.HttpResponse(response)
    
    
    if not isValidMarkRange(mark_1,mark_2,mark_3,mark_4,mark_5):
        responseJSON = {
            "error": True,
            "errormessage": "All marks must be valid integars between 0-100",
            "output": None
        }

        response = json.dumps(responseJSON)
        return func.HttpResponse(response)

    
    output = getMedianMark(mark_1,mark_2,mark_3,mark_4,mark_5)
    responseJSON = {
            "error": False,
            "errormessage": None,
            "output": output
        }
    response = json.dumps(responseJSON)
    return func.HttpResponse(response)

def isValidMarkRange(*marks):
    for mark in marks:
        if not 0 <= mark <=100:
            return False
    return True

#https://qub-grademe-median.azurewebsites.net/api/median/?name=ten&module_1=m1&mark_1=20&module_2=m2&mark_2=90&module_3=m3&mark_3=80&module_4=m4&mark_4=60&module_5=m5&mark_5=60
#http://localhost:7071/api/median?module_1=m1&mark_1=20&module_2=m2&mark_2=90&module_3=m3&mark_3=80&module_4=m4&mark_4=60&module_5=m5&mark_5=60

def getMedianMark(*marks):
    n = len(marks)
    s = sorted(marks)
    return (s[n//2-1]/2.0+s[n//2]/2.0, s[n//2])[n % 2] if n else None