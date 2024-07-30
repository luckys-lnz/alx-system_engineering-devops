#!/usr/bin/python3
"""
Python script using REST API to return info on TODO list progress.
"""
import requests
import sys

if __name__ == '__main__':
    BASE_URL = "https://jsonplaceholder.typicode.com/"

    # Check usage in case of incorrect arguments
    if len(sys.argv) != 2:
        print("Usage: python3 filename.py employee_id")
        sys.exit(1)

    # Use try-except to handle non-integer employee_id
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("employee_id must be an integer")
        sys.exit(1)

    # Fetch user info from the API
    user_response = requests.get(f"{BASE_URL}users/{employee_id}")
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found")
        sys.exit(1)
    user = user_response.json()

    # Fetch TODO info from the API, using params to specify the user ID
    todos_response = requests.get(
        f"{BASE_URL}todos", params={"userId": employee_id}
    )
    if todos_response.status_code != 200:
        print("Could not fetch todos...")
        sys.exit(1)
    todos = todos_response.json()

    # Extract completed tasks
    completed_tasks = [
        task.get('title') for task in todos if task.get('completed') is True
    ]

    total_tasks = len(todos)
    completed_tasks_count = len(completed_tasks)

    # Print the TODO list progress
    print(
        f"Employee {user.get('name')} is done with tasks"
        f"({completed_tasks_count}/{total_tasks}):"
    )
    for task_title in completed_tasks:
        print(f"\t {task_title}")

