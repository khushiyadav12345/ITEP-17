# 3. Employee Management

# Base class Employee.

# Derived:

# Developer
# Tester
# HR

# Calculate salaries differently.

class Employee:
    def salary():
        pass
    
class Developer(Employee):
    def salary(self):
        print("Developer Salary = 5000")
            
class Tester(Employee):
    def salary(self):
        print("Tester Salary = 10000")

class HR(Employee):
    def salary(self):
        print("HR Salary = 15000")
        
developer = Developer()
developer.salary()

tester = Tester()
tester.salary()

hr = HR()
hr.salary()
            