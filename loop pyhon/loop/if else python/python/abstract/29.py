# 29. Employee Attendance

# Abstract:

# Employee

# Derived:

# FullTimeEmployee
# PartTimeEmployee

# Calculate working hours.

from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def workingHours(self):
        pass


class FullTimeEmployee(Employee):
    def workingHours(self):
        hours = 8
        print("Full Time Employee Working Hours =", hours)


class PartTimeEmployee(Employee):
    def workingHours(self):
        hours = 4
        print("Part Time Employee Working Hours =", hours)


f = FullTimeEmployee()
f.workingHours()

p = PartTimeEmployee()
p.workingHours()