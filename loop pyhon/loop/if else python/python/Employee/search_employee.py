from database import load_employees
def search_employee():
    print("---- SEARCH EMPLOYEE BY NAME -----")

    keyword = input("Please enter the name to search: ")

    employee_list = load_employees()

    results = []
    for emp in employee_list:
        if keyword.lower() in emp["name"].lower():
            results.append(emp)

    if len(results) == 0:
        print(f"'{keyword}' sorry this name not found!")
        return

    print(f"\n{len(results)} employee(s) yes its name found:\n")

    for emp in results:
        print("----")
        print(f"ID         : {emp['id']}")
        print(f"Name       : {emp['name']}")
        print(f"Department : {emp['department']}")
        print(f"Position   : {emp['position']}")
        print(f"Salary     : {emp['salary']}")

search_employee()
