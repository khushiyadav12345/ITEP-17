# 25. Ride Booking App

# Abstract:

# Ride

# Derived:

# BikeRide
# CabRide
# AutoRide

# Calculate fare.

from abc import ABC, abstractmethod

class Ride(ABC):

    @abstractmethod
    def calculateFare(self):
        pass


class BikeRide(Ride):
    def calculateFare(self):
        distance = 10
        fare = distance * 5
        print("Bike Ride Fare =", fare)


class CabRide(Ride):
    def calculateFare(self):
        distance = 10
        fare = distance * 15
        print("Cab Ride Fare =", fare)


class AutoRide(Ride):
    def calculateFare(self):
        distance = 10
        fare = distance * 8
        print("Auto Ride Fare =", fare)


b = BikeRide()
b.calculateFare()

c = CabRide()
c.calculateFare()

a = AutoRide()
a.calculateFare()