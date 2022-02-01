#!/usr/bin/python3
""" using https://jsonplaceholder.typicode.com/
API, for a given employee ID, returns information
about his/her TODO list progress in JSON"""

import json
import requests
from sys import argv

if __name__ == '__main__':

    # Getting EMPLOYEE_NAME and USER_ID
    USER_ID = argv[1]
    EMPLOYEE = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(argv[1]))
    EMPLOYEE_NAME = EMPLOYEE.json().get("username")

    # Getting all info into USER_INFO
    TASKS = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(argv[1]))
    TASK_JSON = TASKS.json()
    
    USER_INFO = {USER_ID: [{
                "task": i.get('title'),
                "completed": i.get('completed'),
                "username": EMPLOYEE_NAME} for i in TASK_JSON]}

    # Creating the file and passing onto JSON
    FILE = USER_ID + '.json'

    with open(FILE, 'w') as JSON_FILE:
        json.dump(USER_INFO, JSON_FILE)
