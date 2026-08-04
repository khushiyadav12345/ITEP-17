
# Employee Record System
# Create a class Employee with private fields: id, name, and salary.
# Use setter methods to assign values. Add a method to display employee details.
class Employee:
    def __init__(self):
        self.__id = 0
        self.__name = None
        self.__salary = 0

    def set_values(self,id,name,salary):
        self.__id = id
        self.__name = name
        self.__salary = salary

    def display(self):
        print(self.__id)
        print(self.__name)
        print(self.__salary)
    
obj = Employee()
obj.set_values(1,"Khushi",10000)
obj.display()