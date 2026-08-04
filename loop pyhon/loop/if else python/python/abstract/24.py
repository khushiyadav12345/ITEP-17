# 24. ATM System

# Abstract:

# ATM

# Derived:

# SBIATM
# HDFCATM

# Implement banking operations.

from abc import ABC, abstractmethod

class ATM(ABC):

    @abstractmethod
    def bankingOperation(self):
        pass


class SBIATM(ATM):
    def bankingOperation(self):
        print("SBI ATM: Cash Withdrawal")


class HDFCATM(ATM):
    def bankingOperation(self):
        print("HDFC ATM: Balance Check")


s = SBIATM()
s.bankingOperation()

h = HDFCATM()
h.bankingOperation()