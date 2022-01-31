#!/usr/bin/python3
""" using https://jsonplaceholder.typicode.com/
API, for a given employee ID, returns information
about his/her TODO list progress."""

import requests
from sys import argv

if __name__ == '__main__':

    # Getting Employee name
    EMPLOYEE = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(argv[1]))
    EMPLOYEE_NAME = EMPLOYEE.json().get("name")

    # Getting the task in JSON format and the total ammount of tasks
    TASKS = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(argv[1]))
    TASKS_JSON = TASKS.json()
    TOTAL_NUMBER_OF_TASKS = len(TASKS_JSON)

    # Getting the done tasks
    DONE_TASKS = []
    for i in TASKS_JSON:
        if i.get('completed') is True:
            DONE_TASKS.append(i.get('title'))
            NUMBER_OF_DONE_TASKS = len(DONE_TASKS)

    # Print the first line
    print('Employee {} is done with tasks({}/{}):'.
          format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    # Print done tasks
    for i in DONE_TASKS:
        print('\t {}'.format(i))
