# 27. Transport Fare System

# Abstract:

# Transport

# Derived:

# Train
# Flight
# Bus

# Implement ticket pricing.

from abc import ABC, abstractmethod

class Transport(ABC):

    @abstractmethod
    def ticketPrice(self):
        pass


class Train(Transport):
    def ticketPrice(self):
        distance = 100
        price = distance * 2
        print("Train Ticket Price =", price)


class Flight(Transport):
    def ticketPrice(self):
        distance = 100
        price = distance * 10
        print("Flight Ticket Price =", price)


class Bus(Transport):
    def ticketPrice(self):
        distance = 100
        price = distance * 3
        print("Bus Ticket Price =", price)


t = Train()
t.ticketPrice()

f = Flight()
f.ticketPrice()

b = Bus()
b.ticketPrice()