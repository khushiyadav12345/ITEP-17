from add_employee    import add_employee
from view_employee   import view_employee
from update_employee import update_employee
from delete_employee import delete_employee
from search_employee import search_employee
from select_by_id    import select_by_id


while True:
    print("  EMPLOYEE MANAGEMENT SYSTEM  ")
    print("-----")
    print("1. Add New Employee")
    print("2. View All Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Search by Name")
    print("6. Select by ID")
    print("0. Exit")
    print("-----")

    choice = input("choose your option [0-6]: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employee()
    elif choice == "3":
        update_employee()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        search_employee()
    elif choice == "6":
        select_by_id()
    elif choice == "0":
        print("Program Finish")
        break
    else:
        print("wrong option please try again")
