# 4. Student Grade System
# Problem

# Create a student result management system.

# Requirements

# Each student should have:

# roll number
# name
# marks in 3 subjects
# Functionalities
# Calculate total marks
# Calculate percentage
# Assign grade:
# A → 90+
# B → 75+
# C → 50+
# Fail otherwise
# Track total students
# Concepts Practiced
# instance methods
# conditional logic in classes
# object-based calculations

class Student:
    total_students = 0
    def __init__(self, roll_no, name, technical1, softskill2, aptitude3):
        self.roll_no = roll_no
        self.name = name
        self.technical1 = technical1
        self.softskill2 = softskill2
        self.aptitude3 = aptitude3
        
        Student.total_students += 1
        
    def total_marks(self):
        return self.technical1 + self.softskill2 + self.aptitude3
     
    def percentage(self):
        return self.total_marks()/3
     
    def grade(self):
        per = self.percentage()
        
        if per >= 90:
            return "A"
        elif per >= 75:
            return "B"
        elif per >= 50:
            return "C"
        else:
            return "Fail"

    def display(self):
        print(f"Roll No : {self.roll_no}")
        print(f"Name : {self.name}")
        print(f"Marks : {self.technical1}, {self.softskill2}, {self.aptitude3}")
        print(f"Total Marks : {self.total_marks()}")
        print(f"Percentage : {self.percentage():}")
        print(f"Grade : {self.grade()}")

Student1 = Student(200, "Ram", 95, 90, 92)
Student2 = Student(201, "Shyaam", 80, 78, 76)
Student3 = Student(202, "Gyan", 45, 50, 40)
Student4 = Student(203, "Nishi", 96, 99, 95)
Student5 = Student(204, "Nandini", 99, 96, 93)


Student1.display()
print()

Student2.display()
print()

Student3.display()
print()

Student4.display()
print()

Student5.display()
print()

print("Total Students :", Student.total_students)
            
        
    
    
        
        
    
    
    
    