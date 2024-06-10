import logging

import azure.functions as func

import os
import pyodbc
import struct
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    danielsazuredatabase = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:qubgrademe-database-40230007.database.windows.net,1433;Database=qubgrademe-database;Uid=azureuser;Pwd={Password99.};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
    conn = pyodbc.connect(danielsazuredatabase)

    typeOfRequest = req.params.get('typeOfRequest')
    username = req.params.get('username')
    # check type of request was proviced
    if not typeOfRequest:
        responseJSON = {
                    "error": True,
                    "errormessage": "Type of request was not provided",
                    "output": None
                }
        response = json.dumps(responseJSON)
        return func.HttpResponse(response,status_code=400)
    # check username was proviced
    if not username:
        responseJSON = {
                    "error": True,
                    "errormessage": "Username was not provided",
                    "output": None
                }
        response = json.dumps(responseJSON)
        return func.HttpResponse(response,status_code=400)

    # F. Stateful Saving of Current Values
    # Provide the option to enter an identifier and thus recall the saved items to the front-end.

    if typeOfRequest == 'get':
        query = f'''SELECT * FROM Person WHERE username = '{username}' '''
        with conn.cursor() as cursor:
            cursor.execute(query)        
            logging.info(cursor.description)
            columns = cursor.description
            allRows = [{columns[index][0]:column for index, column in enumerate(
                value)} for value in cursor.fetchall()]
            
        #If username doesnt exist in database     
        if allRows==[]:
            responseJSON = {
                    "error": True,
                    "errormessage": "Username does not exist",
                    "output": None
                }
            response = json.dumps(responseJSON)
            return func.HttpResponse(response,status_code=400)
        
        #Get the user data and parse it
        userData = allRows[0]
        responseJSON = {
            "error": False,
            "errormessage": None,
            "output": f"You have retrieved {username} successfully",
            "mark_1": userData['mark_1'],
            "mark_2": userData['mark_2'],
            "mark_3": userData['mark_3'],
            "mark_4": userData['mark_4'],
            "mark_5": userData['mark_5'],
            "module_1": userData['module_1'],
            "module_2": userData['module_2'],
            "module_3": userData['module_3'],
            "module_4": userData['module_4'],
            "module_5": userData['module_5'],
            "result": userData['results']
        }
        response = json.dumps(responseJSON)
        return func.HttpResponse(response, status_code=200)

    # F. Stateful Saving of Current Values
    # Save the current modules, marks, and the results (and display) an identifier for the saved items.
    if typeOfRequest == 'send':
        rmark_1 = req.params.get('mark_1')
        rmark_2 = req.params.get('mark_2')
        rmark_3 = req.params.get('mark_3')
        rmark_4 = req.params.get('mark_4')
        rmark_5 = req.params.get('mark_5')
        module_1 = req.params.get('module_1')
        module_2 = req.params.get('module_2')
        module_3 = req.params.get('module_3')
        module_4 = req.params.get('module_4')
        module_5 = req.params.get('module_5')
        
        # sort = req.params.get('sort')
        # maxmin = req.params.get('maxmin')
        total = req.params.get('total')
        classify = req.params.get('classify')
        average = req.params.get('average')
        median = req.params.get('median')        
        resultsString = f'Total = {total}\nClassify = {classify}\nAverage = {average}\nMedian = {median}'

        # ERROR HANDLING - Ensure marks are valid integars
        try:
            mark_1 = int(rmark_1)
            mark_2 = int(rmark_2)
            mark_3 = int(rmark_3)
            mark_4 = int(rmark_4)
            mark_5 = int(rmark_5)
        except ValueError:
            responseJSON = {
                "error": True,
                "errormessage": "Invalid mark provided (must be int)",
                "output": None
            }
            response = json.dumps(responseJSON)
            return func.HttpResponse(response)


        ## ERROR HANDLIND - Check modules are valid
        modules = {module_1, module_2, module_3, module_4, module_5}
        count = 0
        for module in modules:
            count += 1
            if not module:
                responseJSON = {
                    "error": True,
                    "errormessage": f"Module {count} is invalid",
                    "output": None
                }
                response = json.dumps(responseJSON)
                return func.HttpResponse(response, status_code=200)

        ## Send request to azure database to either update the usernames data else create a new Person with the username
        query = f'''IF EXISTS (SELECT * FROM Person WHERE username = '{username}') BEGIN UPDATE Person SET module_1 = '{module_1}', module_2= '{module_2}', module_3= '{module_3}', module_4= '{module_4}', module_5= '{module_5}', mark_1= {mark_1}, mark_2 = {mark_2}, mark_3= {mark_3}, mark_4= {mark_4}, mark_5= {mark_5}, results= '{resultsString}' WHERE username = '{username}'; END ELSE BEGIN INSERT INTO Person (username, module_1, module_2, module_3, module_4, module_5, mark_1, mark_2, mark_3, mark_4, mark_5, results) VALUES ('{username}', '{module_1}', '{module_2}','{module_3}','{module_4}','{module_5}', {mark_1},{mark_1},{mark_3},{mark_4},{mark_5}, '{resultsString}'); END'''
        with conn.cursor() as cursor:
            cursor.execute(query)  # works!
        responseJSON = {
                    "error": False,
                    "errormessage": None,
                    "output": f"Successfully stored data for {username}"
                }
        response = json.dumps(responseJSON)
        return func.HttpResponse(response, status_code=200)

    # ERROR HANDLING - if type of request was invalid
    responseJSON = {
                    "error": True,
                    "errormessage": "Type of request was invalid",
                    "output": None
                }
    response = json.dumps(responseJSON)
    return func.HttpResponse(response,status_code=400)
