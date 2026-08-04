# 7. Hospital Patient Record System
# Problem

# Create a patient management system.

# Requirements

# Each patient should contain:

# patient id
# name
# disease
# doctor assigned
# Functionalities
# Display patient details
# Change doctor
# Count total patients admitted
# Additional Task

# Create patient from formatted string using class method.


class Hospital:
    total__patients = 0
    def __init__(self,id,name,disease,doctor):
        self.__id = id
        self.__name = name
        self.__disease = disease
        self.__doctor = doctor
        
        Hospital.total_patients += 1
        
    def display(self):
        print(f"Patient Id : {self.patient_id}")
        print(f"Name : {self.name}")
        print(f"Disease : {self.disease}")
        print(f"Doctor : {self.doctor}")
        print()
        
    def change_doctor(self, new_doctor):
        self.doctor = new_doctor
        print(f"Doctor changed to {new_doctor}")
        
p1 = id(101, "Monu", "Fever", "Dr.mina")
p2 = id(102, "Kanu", "cancer", "Dr.riya")
p3 = id(103, "Ranu", "diabetis","Dr.neha")

p1.display
p2.display
p3.display

p1.change_doctor("Dr.verma")

p1.display()

print("Total Patients :", id.total_patients)


    
        