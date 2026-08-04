# 5. Library Management System
# Problem

# Design a library system.

# Requirements

# Each book should contain:

# book id
# title
# author
# availability status
# Functionalities
# Issue book
# Return book
# Display availability
# Count total books using class variable
# Additional Challenge

# Prevent issuing already issued books.

# Concepts Practiced
# object state changes
# boolean flags
# class variables

class Book:
    def __init__(self,id,title,author):
        self.__id = id
        self.__title = title
        self.__author = author
        self.__status = True  
    
    def issue(self):
        if self.is_available():
            print(f"Book issued...")
            self.__status = False
        else:
            print(f"Book not available...")        
    
    def is_available(self):
        return self.__status

    def submit(self):
        if not self.is_available():
            self.__status = True
            print(f"Book Returned..")
        else:
            print(f"Book not issued")     

b1 = Book(100,"Java","Patrik norton")
print(f"{"Book Available" if b1.is_available() else "Not Avaialble"}")
b1.issue()
b1.submit()            