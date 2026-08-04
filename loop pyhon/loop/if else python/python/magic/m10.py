# 10. Company Department System
# Problem

# Create:

# Department
# Employee

# classes.

# Requirements

# Each department:

# has department name
# stores employee objects
# Functionalities
# Add employee to department
# Display all employees
# Calculate total department salary
# Concepts Practiced
# object composition
# object interaction
# storing objects in lists


class Department:
    def __init__(self,name):
        self.__name = name
        self.__employees = []

    def add_employee(self,e):
        self.__employees.append(e)

    def display(self):
        for emp in self.__employees:
            print(emp)

class Employee:
    def __init__(self,id,name,salary):
        self.__id = id
        self.__name = name
        self.__salary = salary   
    
    def __str__(self):
        return str(self.__id) + " : "+self.__name+" : "+ str(self.__salary)

d1 = Department("Manager")
d2 = Department("HR")

e1 = Employee(id=100,salary=50000,name="Chiku")
e2 = Employee(id=101,name="Piku",salary=2000)

e3 = Employee(id=102,name="Niku",salary=4000)
e4 = Employee(id=103,name="Kiku",salary=8000)

d1.add_employee(e1)
d1.add_employee(e2)

d2.add_employee(e3)
d2.add_employee(e4)

d1.display()
print("="*50)
d2.display()