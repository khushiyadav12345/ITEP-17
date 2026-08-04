# 13. Exam Portal
# Problem

# Create exam management system.

# Requirements

# Each exam object:

# exam name
# total marks
# passing marks
# Functionalities
# Check pass/fail
# Calculate grade
# Maintain total exams conducted

class Exam:
    def __init__(self,name,total_marks,passing_marks):
        self.__Name = name
        self.__Total_marks = total_marks
        self.__passing_marks = passing_marks