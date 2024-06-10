from flask import Flask
from flask import request
from flask import Response
import json

import classifygrade

app = Flask(__name__)


@app.route('/')
def classify():
    rmark1 = request.args.get('mark_1')
    rmark2 = request.args.get('mark_2')
    rmark3 = request.args.get('mark_3')
    rmark4 = request.args.get('mark_4')
    rmark5 = request.args.get('mark_5')


# missing parameter error
    if not rmark1:
        r = {
            "error": True,
            "errormessage": "Mark 1 was not provided",
            "output": None
        }
        reply = json.dumps(r)
        response = Response(response=reply, status=400,
                            mimetype='application/json')
        return response
    if not rmark2:
        r = {
            "error": True,
            "errormessage": "Mark 2 was not provided",
            "output": None
        }
        reply = json.dumps(r)
        response = Response(response=reply, status=400,
                            mimetype='application/json')
        return response
    if not rmark3:
        r = {
            "error": True,
            "errormessage": "Mark 3 was not provided",
            "output": None
        }
        reply = json.dumps(r)
        response = Response(response=reply, status=400,
                            mimetype='application/json')
        return response
    if not rmark4:
        r = {
            "error": True,
            "errormessage": "Mark 4 was not provided",
            "output": None
        }
        reply = json.dumps(r)
        response = Response(response=reply, status=400,
                            mimetype='application/json')
        return response
    if not rmark5:
        r = {
            "error": True,
            "errormessage": "Mark 5 was not provided",
            "output": None
        }
        reply = json.dumps(r)
        response = Response(response=reply, status=400,
                            mimetype='application/json')
        return response


# string conversion error
    try:
        mark_1 = int(rmark1)
        mark_2 = int(rmark2)
        mark_3 = int(rmark3)
        mark_4 = int(rmark4)
        mark_5 = int(rmark5)
    except ValueError:
        r = {
            "error": True,
            "errormessage": "Invalid mark provided (must be int)",
            "output": None
        }
        reply = json.dumps(r)
        response = Response(response=reply, status=400,
                            mimetype='application/json')
        return response

    if not classifygrade.checkValidMark(mark_1, mark_2, mark_3, mark_4, mark_5):
        r = {
            "error": True,
            "errormessage": "All marks must be valid integars between 0-100",
            "output": None
        }
        reply = json.dumps(r)
        response = Response(response=reply, status=400,
                            mimetype='application/json')
        return response
    
    average = classifygrade.averagemark(mark_1, mark_2, mark_3, mark_4, mark_5)
    classification = classifygrade.classifygrade(average)
    r = {
        "error": False,
        "errormessage": None,
        "output": classification
    }
    reply = json.dumps(r)
    response = Response(response=reply, status=200,
                        mimetype='application/json')
    response.headers["Content-Type"] = "application/json"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# ?module_1=m1&mark_1=50&module_2=m2&mark_2=90&module_3=m3&mark_3=80&module_4=m4&mark_4=60&module_5=m5&mark_5=70
