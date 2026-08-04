# 12. University System
# Person
# Student(Person)
# GraduateStudent(Student)

# Add thesis information.

class Person:
    def information(self):
        print("Person is at base level")

class Student(Person):
    def information(self):
        print("student is a person")

class GraduateStudent(Student):
    def information(self):
        print("GraduateStudent is a student")
        
    def thesis(self):
        print("Thesis topic : Data Science")
        
g = GraduateStudent()
g.information()
g.thesis()