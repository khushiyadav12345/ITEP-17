from database import load_employees

def view_employee():
    print("\n----- ALL EMPLOYEES -----")

    employee_list = load_employees()

    if len(employee_list) == 0:
        print("No employee records available.")
        return

    for emp in employee_list:
        print("-------")
        print(f"ID         : {emp['id']}")
        print(f"Name       : {emp['name']}")
        print(f"Department : {emp['department']}")
        print(f"Position   : {emp['position']}")
        print(f"Salary     : {emp['salary']}")

    print("--------")
    print(f"Total Employees: {len(employee_list)}")

view_employee()
