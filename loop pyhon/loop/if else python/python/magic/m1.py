class Employeee:
    __counter = 0
    def __init__(self,id,name,department,salary):
        self.__id = id
        self.__name = name
        self.__department = department
        self.__salary = int(salary)
        Employeee.__counter += 1
        
    def display(self):
        print(f"Id : {self.__id}\n Name : {self.__name}\n Department : {self.__department}\n Salary : {self.__salary}")
        
    def increment_salary(self,per):
        self.__salary += (self.__salary*per)/100
        
    @classmethod
    def from_string(cls,emp_data):
        
        id,name,department,salary = emp_data.split("-")
        return cls(id,name,department,salary)
    @classmethod
    def total_employeee(cls):
        return Employeee.__counter
    
e1 = Employeee.from_string("101-Rahul-IT-50000")
e1.increment_salary(10)

e2 = Employeee.from_string("102-chinu-CS-100000")
e2.increment_salary(20)

e1.display()
e2.display()

print("Total Employeee :", Employeee.total_employeee())
        
# 1. Employee Management System
# Problem

# Create an Employee class to manage employee details.

# Requirements

# Each employee should have:

# employee id
# name
# department
# salary
# Functionalities
# Display employee details
# Increase salary by percentage
# Count total employees created using a class variable

# Create employee object from a string:

# "101-Rahul-IT-50000"

# using a class method.

# Concepts Practiced
# constructor
# instance variables
# class variables
# class method
# instance methods
