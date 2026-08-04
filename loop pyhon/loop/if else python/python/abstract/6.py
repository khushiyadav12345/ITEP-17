# 6. Hospital Management

# Parent:

# HospitalStaff

# Child:

# Doctor
# Nurse
# Receptionist

# Implement duties().

class HospitalStaff:
    def duties(self):
        pass

class Doctor(HospitalStaff):
    def duties(self):
        print("doctor checks the patient")
        
class Nurse(HospitalStaff):
    def duties(self):
        print("nurse helps the doctor")
        
class Receptionist(HospitalStaff):
    def duties(self):
        print("receptionlist keeps all record")
        
doctor = Doctor()
doctor.duties()

nurse = Nurse()
nurse.duties()

receptionist = Receptionist()
receptionist.duties()
    
