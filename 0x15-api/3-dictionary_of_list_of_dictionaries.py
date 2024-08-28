#!/usr/bin/python3
"""A REST API implementation to fetch todos and save in json file"""
import json
import requests

if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    data = {}
    for user in users:
        user_id = user.get('id')
        todos_url = ('https://jsonplaceholder.typicode.com/users/{}/todos'
                     .format(user_id))

        tasks = requests.get(todos_url).json()
        data[user_id] = [{
            "username": user.get('username'),
            "task": task.get('title'),
            "completed": task.get('completed')
        } for task in tasks]

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file)
