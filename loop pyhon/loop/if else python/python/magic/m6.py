# 6. Movie Ticket Booking System
# Problem

# Create a movie booking system.

# Requirements

# Each movie should have:

# movie name
# total seats
# available seats
# Functionalities
# Book tickets
# Cancel tickets
# Prevent overbooking
# Display seat availability
# Concepts Practiced
# state updates
# validations
# object behavior




# movie:
#     property [moviename, totalseats]
#     behaviour[total seats, book tickets(), cancel tickets(), is_available]

class Movie:
    def __init__(self,moviename,totalseats,availableseats):
        self.__moviename = moviename
        self.__totalseats = totalseats
        self.__availableseats = availableseats
        
    def get_price(self):
        return self.__price
    
    def get_moviename(self):
        return self.__moviename
    
    def get__timing(self):
        return self.__timing