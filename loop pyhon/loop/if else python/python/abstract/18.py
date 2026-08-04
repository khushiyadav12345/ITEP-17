# 18. Vehicle Insurance System
# Vehicle
# InsuredVehicle
# Car

# Calculate insurance amount.

class Vehicle:
    def __init__(self, price):
        self.price = price

class InsuredVehicle(Vehicle):
    def insurance(self):
        print("Insurance available")

class Car(InsuredVehicle):
    def calculateInsurance(self):
        amount = self.price * 10 / 100
        print("Insurance Amount =", amount)

c = Car(10000)

c.insurance()
c.calculateInsurance()