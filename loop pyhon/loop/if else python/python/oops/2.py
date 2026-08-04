# Book Library
# Create a class Book with fields: title, author, and price.
# Use setters to assign values and a method to print book details.

class Library:
    def __init__(self):
        self.__tittle = 0
        self.__author = None
        self.__price = 0

    def set_values(self,tittle,author,price):
        self._tittle = tittle
        self.__author = author
        self.__price = price

    def display(self):
        print(self.__tittle)
        print(self.__author)
        print(self.__price)
    
obj = Library()
obj.set_values(1,"Khushi",10000)
obj.display()