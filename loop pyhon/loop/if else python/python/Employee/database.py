import json
import os

FILE_NAME = "employees.json"

def load_employees():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as f:
        data = json.load(f)  
    return data

def save_employees(employee_list):
    with open(FILE_NAME, "w") as f:
        json.dump(employee_list, f, indent=4)  

def get_next_id(employee_list):
    if len(employee_list) == 0:
        return 1
    max_id = 0
    for emp in employee_list:
        if emp["id"] > max_id:
            max_id = emp["id"]
    return max_id + 1
