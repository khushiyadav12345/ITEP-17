# 2. Vehicle System

# Create parent class Vehicle.

# Child classes:

# Car
# Bike
# Bus

# Add methods:

# start()
# stop()

class Vehicle:
    def start():
      pass
    def stop():
      pass
 
class Car(Vehicle):
    def start(self):
        print("car started")
    def stop(self):
        print("car stop")
    
class Bike(Vehicle):
    def start(self):
        print("bike started")
    def stop(self):
        print("bike stop")
    
car = Car()
car.start()
car.stop()


bike = Bike()
bike.start()
bike.stop()
