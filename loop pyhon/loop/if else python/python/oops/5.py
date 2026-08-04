# Product Inventory
# Create a class Product with fields: productId, name, quantity, price.
# Use setters to assign values. Add a method to calculate total value (quantity * price).

class Product:
    def __init__(self):
        self.__productId = 0
        self.__name = None
        self.__quantity = 0
        self.__price = 0

    def set_values(self,productId,name,quantity,price):
        self.__productId = productId
        self.__name = name
        self.__quantity = quantity
        self.__price = price

    def calculate_total_value(self):
        total_value = self.__quantity * self.__price
        return total_value
# print(f"Total value of the product is : { self.calculate_total_value()}")