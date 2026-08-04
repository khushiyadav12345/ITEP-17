# 7. Shopping Cart System

# Base:

# Product

# Derived:

# Electronics
# Grocery
# Clothing

# Apply discounts.

class Product:
    def discount(self,price):
        pass

class Electronics(Product):
    def discount(self,price):
        print("Discounted price is ", price - (price * 10/100))
        
class Grocery(Product):
    def discount(self,price):
        print("Grocery price is ", price - (price * 2/100) )

class Clothing(Product):
    def discount(self,price):
        print("Clothing price is ", price - (price * 10/100))

e = Electronics()
e.discount(1000)

e = Grocery()
e.discount(200)

e = Clothing()
e.discount(5000)
