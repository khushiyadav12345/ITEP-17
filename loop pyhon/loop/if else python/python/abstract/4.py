# 4. Student Management

# Base class Person.

# Derived:

# Student
# Teacher

# Add role-specific methods.

class Person:
    def role(self):
        pass

class Student(Person):
    def study(self):
        print("student is studying")
        
class Teacher(Person):
    def teach(self):
        print("teacher is teach")
        
student = Student()
student.study()

teacher = Teacher()
teacher.teach()
