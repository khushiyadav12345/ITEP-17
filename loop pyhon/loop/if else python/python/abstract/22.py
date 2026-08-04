# 22. Payment Gateway

# Abstract class Payment.

# Derived:

# CreditCard
# UPI
# Wallet

# Implement payment processing.

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def processPayment(self):
        pass


class CreditCard(Payment):
    def processPayment(self):
        print("Payment done using Credit Card")


class UPI(Payment):
    def processPayment(self):
        print("Payment done using UPI")

class Wallet(Payment):
    def processPayment(self):
        print("Payment done using Wallet")

c = CreditCard()
c.processPayment()

u = UPI()
u.processPayment()

w = Wallet()
w.processPayment()