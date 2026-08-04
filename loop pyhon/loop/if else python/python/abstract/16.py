# 16. E-commerce User Roles
# User
# Seller(User)
# PremiumSeller(Seller)

# Add premium benefits.

class User:
    def login(self):
        print("User logged in")

class Seller(User):
    def sellProduct(self):
        print("Seller can sell products")

class PremiumSeller(Seller):
    def premiumBenefits(self):
        print("Premium seller gets extra benefits")

p = PremiumSeller()

p.login()
p.sellProduct()
p.premiumBenefits()