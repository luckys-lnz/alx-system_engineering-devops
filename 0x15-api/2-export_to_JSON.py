#!/usr/bin/python3
"""
Python script using REST API to return info on TODO list progress.
"""
import json
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

    # format in which data will be displayed
    user_data = {
        str(employee_id): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            }
            for task in todos
        ]
    }

    # Define JSON file name
    filename_json = f"{employee_id}.json"

    # Write data to JSON file, with good Indenting,Checker might red-flag me
    with open(filename_json, mode='w', encoding='utf-8') as jsonfile:
        json.dump(user_data, jsonfile, indent=4)

    print(f"Data exported to {filename_json}")
