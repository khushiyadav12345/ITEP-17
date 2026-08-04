
# 8. Online Food Delivery

# Parent:

# FoodItem

# Derived:

# Pizza
# Burger
# Sandwich

# Calculate total bill.

class FoodItem:
    def __init__(self,name,price,quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
    
    def get_price(self):
        return self.__price
    
    def get_quantity(self):
        return self.__quantity
        
class Pizza(FoodItem):
    def totalbill(self):
        total = self.get_price() * self.get_quantity()
        print(f"total bill of pizza : {total}")
        
class Burger(FoodItem):
    def totalbill(self):
        total = self.get_price() * self.get_quantity()
        print(f"total bill of Burger : {total}")

class Sandwich(FoodItem):
    def totalbill(self):
        total = self.get_price() * self.get_quantity()
        print(f"total bill of Sandwich : {total}")

p = Pizza("corn Pizza",100, 2)
b = Burger("veg burger",200,3)
s = Sandwich("Paneer sandwich",50,2)

p.totalbill()
b.totalbill()
s.totalbill()