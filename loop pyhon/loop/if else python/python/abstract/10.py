
# 10. Movie Ticket Booking

# Parent:

# Ticket

# Derived:

# GoldTicket
# PlatinumTicket
# VIPTicket

# Apply pricing logic.

class Ticket:
    def pricing(self):
        pass
    
class GoldTicket(Ticket):
    def pricing(self):
        print("Gold Ticket price is : 500 rs")
        
class PlatinumTicket(Ticket):
    def pricing(self):
        print("Platinum Ticket is : 300 rs")
        
class VIPTicket(Ticket):
    def pricing(self):
        print("VIP Ticket is : 100 rs")
        
g = GoldTicket()
g.pricing()

p = PlatinumTicket()
p.pricing()

v = VIPTicket()
p.pricing()
    