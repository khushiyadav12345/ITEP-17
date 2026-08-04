
from database import load_employees, save_employees

def update_employee():
    print("\n----- UPDATE EMPLOYEE -----")

    employee_list = load_employees()

    if len(employee_list) == 0:
        print("No records available for update.")
        return

    emp_id = int(input(" Enter the Employee ID to update : "))

    found = False
    for emp in employee_list:
        if emp["id"] == emp_id:
            found = True
            print(f"\nCurrent Details:")
            print(f"  Name       : {emp['name']}")
            print(f"  Department : {emp['department']}")
            print(f"  Position   : {emp['position']}")
            print(f"  Salary     : {emp['salary']}")

            print("\n Enter new values (leave blank to keep current value):")

            new_name = input(f"New Name       [{emp['name']}]: ")
            new_dept = input(f"New Department [{emp['department']}]: ")
            new_pos  = input(f"New Position   [{emp['position']}]: ")
            new_sal  = input(f"New Salary     [{emp['salary']}]: ")
            if new_name != "":
                emp["name"] = new_name
            if new_dept != "":
                emp["department"] = new_dept
            if new_pos != "":
                emp["position"] = new_pos
            if new_sal != "":
                emp["salary"] = new_sal
            break

    if not found:
        print(f"ID {emp_id} sorry this ID not found!")
        return
    save_employees(employee_list)
    print(f"\n Employee ID {emp_id} update successfully!")


update_employee()
