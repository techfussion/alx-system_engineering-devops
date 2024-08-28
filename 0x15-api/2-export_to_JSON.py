#!/usr/bin/python3
"""A REST API implementation to fetch employee todos and save it to
json file"""

import json
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
    data = {user_id: [
        {"task": task.get('title'),
         "completed": task.get('completed'),
         "username": user.get('username')}
        for task in tasks]}

    with open('{}.json'.format(user_id), 'w') as json_file:
        json.dump(data, json_file)
