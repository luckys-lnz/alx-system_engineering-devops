#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import requests
import json


def fetch_data():
    """Fetch data from the JSONPlaceholder API"""
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)
    if users_response.status_code != 200 or todos_response.status_code != 200:
        raise Exception("Error fetching data from API")
    users = users_response.json()
    todos = todos_response.json()
    return users, todos


def organize_data(users, todos):
    """Organize data into a dictionary of lists of dictionaries"""
    user_tasks = {}

    for todo in todos:
        user_id = str(todo['userId'])
        if user_id not in user_tasks:
            user_tasks[user_id] = []

        user = next((user for user in users if user[
            'id'] == todo['userId']), {})
        user_tasks[user_id].append({
            "username": user.get('username', ''),
            "task": todo['title'],
            "completed": todo['completed']
        })
    return user_tasks


def save_to_json(data):
    """Save the organized data to a JSON file"""
    filename_json = 'todo_all_employees.json'
    with open('filename_json', 'w') as file:
        json.dump(data, file)
    print(f"Data exported to {filename_json}")


def main():
    users, todos = fetch_data()
    organized_data = organize_data(users, todos)
    save_to_json(organized_data)


if __name__ == "__main__":
    main()
