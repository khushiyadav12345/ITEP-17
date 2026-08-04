# 41. Cab Booking Application

# Features:

# User booking
# Driver assignment
# Fare calculation

# Use:

# inheritance
# abstraction
# polymorphism

import abc
class CabBooking(abc.ABC):
    @abc.abstractmethod
    def book_cab(self):
        pass

    @abc.abstractmethod
    def assign_driver(self):
        pass

    @abc.abstractmethod
    def calculate_fare(self):
        pass
    
class Uber(CabBooking):
    def book_cab(self):
        print("Booking a cab through Uber...")

    def assign_driver(self):
        print("Assigning a driver for Uber...")   
        
    def calculate_fare(self):
        print("Calculating fare for Uber...")
        
class Lyft(CabBooking):
    def book_cab(self):
        print("Booking a cab through Lyft...")

    def assign_driver(self):
        print("Assigning a driver for Lyft...")   
        
    def calculate_fare(self):
        print("Calculating fare for Lyft...")
        
uber_booking = Uber()
uber_booking.book_cab()
uber_booking.assign_driver()
uber_booking.calculate_fare()
lyft_booking = Lyft()
lyft_booking.book_cab()
lyft_booking.assign_driver()
lyft_booking.calculate_fare()

