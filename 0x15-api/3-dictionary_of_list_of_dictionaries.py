#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    data = {}
    for user in users:
        user_id = user["id"]
        todos = requests.get(url + "todos", params={"userId": user_id}).json()
        user_data = [{
            "username": user["username"],
            "task": todo["title"],
            "completed": todo["completed"]}
            for todo in todos]
        data[user_id] = user_data

    filename = "todo_all_employees.json"
    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile)
