# 11. Company Hierarchy
# Person
# Employee(Person)
# Manager(Employee)

# Display company hierarchy.


class Person:
    def hierarchy(self):
        print("Person is at base level")

class Employee(Person):
    def hierarchy(self):
        print("Employee works in company")

class Manager(Employee):
    def hierarchy(self):
        print("Manager manages employees")
        
m = Manager()
m.hierarchy()