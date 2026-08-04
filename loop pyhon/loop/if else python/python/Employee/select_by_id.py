from database import load_employees

def select_by_id():
    print("\n----- SELECT EMPLOYEE BY ID -----")

    emp_id = int(input(" Enter the Employee ID : "))

    employee_list = load_employees()

    found_emp = None
    for emp in employee_list:
        if emp["id"] == emp_id:
            found_emp = emp
            break

    if found_emp is None:
        print(f"ID {emp_id} sorry this ID not found!")
        return

    print("\n----- Employee Details -----")
    print(f"ID         : {found_emp['id']}")
    print(f"Name       : {found_emp['name']}")
    print(f"Department : {found_emp['department']}")
    print(f"Position   : {found_emp['position']}")
    print(f"Salary     : {found_emp['salary']}")
    
select_by_id()
