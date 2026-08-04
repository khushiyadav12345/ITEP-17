# 11. E-Commerce Product System
# Problem

# Create product system for online store.

# Requirements

# Each product should have:

# product name
# price
# category
# Functionalities
# Apply GST using static method
# Apply category discount
# Display final price
# Concepts Practiced
# static methods
# calculations
# reusable 

class Product:
    def __init__(self,name,price,category):
        self.__name = name
        self.__price = price
        self.__category = category
        
    @staticmethod
    def apply_gst(price):
        gst = price * 0.18   
        return price + gst

    def category_discount(self):
        
        if self.category.lower() == "electronics":
            return 10  
        
        elif self.category.lower() == "clothing":
            return 20  
        
        else:
            return 5   
    def final_price(self):
        
        gst_price = Product.apply_gst(self.price)
        discount = self.category_discount()

        final = gst_price - (gst_price * discount / 100)
        
        return final

  
    def display(self):
        print("Product Name :", self.productname)
        print("Category :", self.category)
        print("Original Price :", self.price)
        print("Final Price :", round(self.final_price(), 2))


p1 = Product("Laptop", 50000, "Electronics")
p2 = Product("T-Shirt", 2000, "Clothing")
p3 = Product("Book", 500, "Education")


p1.display()
print()

p2.display()

print()

p3.display()    