
from database import load_employees, save_employees

def delete_employee():
    print("\n----- DELETE EMPLOYEE -----")

    employee_list = load_employees()

    if len(employee_list) == 0:
        print("Koi record nahi hai delete karne ke liye.")
        return

    emp_id = int(input("Kis employee ko delete karna hai (ID dalna paregi): "))

    found_emp = None
    for emp in employee_list:
        if emp["id"] == emp_id:
            found_emp = emp
            break

    if found_emp is None:
        print(f"ID {emp_id} ka employee nahi mila!")
        return

    print(f"\nEmployee mila: {found_emp['name']} | {found_emp['department']}")
    confirm = input("Pakka delete karna hai h na (yes/no): ")

    if confirm == "yes":
        employee_list.remove(found_emp)   
        save_employees(employee_list)    
        print(f"\n '{found_emp['name']}' delete ho gaya ab!")
    else:
        print("Delete cancel kar diya ap ke kehne pr.")


delete_employee()
