from database import load_employees, save_employees, get_next_id
def add_employee():
    print("------ADD NEW EMPLOYEE-----")
    name       = input("Name       : ")
    department = input("Department : ")
    position   = input("Position   : ")
    salary     = input("Salary     : ")

    employee_list = load_employees()

    new_emp = {
        "id"         : get_next_id(employee_list),
        "name"       : name,
        "department" : department,
        "position"   : position,
        "salary"     : salary
    }

    employee_list.append(new_emp)

    save_employees(employee_list)

    print(f"\n '{name}' Add Successfully! ID: {new_emp['id']}")

add_employee()
