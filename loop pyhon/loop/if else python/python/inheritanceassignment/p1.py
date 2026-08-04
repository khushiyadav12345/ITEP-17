# 1. Employee Bonus Calculator
# Problem Statement

# A company gives bonuses differently based on employee type.

# Create:

# abstract class Employee
# child classes:
# Developer
# Manager
# Intern

# Rules:

# Developer → 20% bonus
# Manager → 35% bonus
# Intern → fixed ₹5000 bonus
# Requirements

# Methods:

# calculate_bonus()
# display_details()
# Concepts
# Abstract class
# Method overriding
# Business logic

import abc
class Employee(abc.ABC):
    @abc.abstractmethod
    def calculate_bonus(self):
        pass

    @abc.abstractmethod
    def display_details(self):
        pass
class Developer(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def calculate_bonus(self):
        return self.salary * 0.20
    
    def display_details(self):
        print(f"Developer: {self.name}, Salary: {self.salary}, Bonus: {self.calculate_bonus()}")
class Manager(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def calculate_bonus(self):
        return self.salary * 0.35
    
    def display_details(self):
        print(f"Manager: {self.name}, Salary: {self.salary}, Bonus: {self.calculate_bonus()}")
class Intern(Employee):
    def __init__(self, name):
        self.name = name
        
    def calculate_bonus(self):
        return 5000
    
    def display_details(self):
        print(f"Intern: {self.name}, Bonus: {self.calculate_bonus()}")
dev = Developer("Alice", 80000)
mgr = Manager("Bob", 120000)
intern = Intern("Charlie")
dev.display_details()
mgr.display_details()
intern.display_details()
    