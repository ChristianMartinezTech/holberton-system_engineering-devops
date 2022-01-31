#!/usr/bin/python3
""" using https://jsonplaceholder.typicode.com/
API, for a given employee ID, returns information
about his/her TODO list progress in CSV"""

import csv
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

    USER_INFO = []
    for i in TASK_JSON:
        TASK_COMPLETED_STATUS = i.get("completed")
        TASK_TITLE = i.get("title")
        USER_INFO.append([USER_ID, EMPLOYEE_NAME, TASK_COMPLETED_STATUS,
                          TASK_TITLE])

    # Creating the file and passing onto csv
    FILE_NAME = argv[1] + '.csv'

    with open(FILE_NAME, 'w') as csvfile:
        FILE = csv.writer(
            csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        FILE.writerows(USER_INFO)
