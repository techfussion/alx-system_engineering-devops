#!/usr/bin/python3
"""A REST API implementation to fetch employee info"""

import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    user_url = ('https://jsonplaceholder.typicode.com/users/{}'
                .format(user_id))
    todos_url = ('https://jsonplaceholder.typicode.com/users/{}/todos'
                 .format(user_id))

    user = requests.get(user_url).json()
    tasks = requests.get(todos_url).json()
    completed_tasks = list(filter(lambda t: t.get('completed'), tasks))

    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(completed_tasks), len(tasks)))

    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
