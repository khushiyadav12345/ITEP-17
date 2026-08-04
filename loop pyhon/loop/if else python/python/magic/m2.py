# 2. Bank Account Simulation
# Problem

# Design a banking system using OOP.

# Requirements

# Each account should contain:

# account number
# holder name
# balance
# Functionalities
# Deposit money
# Withdraw money
# Prevent withdrawal if balance insufficient
# Display account summary
# Maintain bank-wide interest rate as class variable
# Add static method to validate minimum balance rule
# Concepts Practiced
# object state management
# static methods
# class variables
# validations

class BankAccount:
    total_Bank = 0
    def __init__(self, account_num, holder_name, balance):
        self.account_num = account_num
        self.holder_name = holder_name
        self.balance = balance
        
        BankAccount.total_Bank += 1
        
    def display(self):
        print(f"account_num : {self.account_num}")
        print(f"holder_name : {self.holder_name}")
        print(f"balance : {self.balance}")
        
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully")
        
    def withdraw(self, amount):
        if self.balance - amount >= 1000:
            self.balance -= amount
            print(f"{amount} withdrawn successfully")
        else:
            print("insufficient balance")
            
    @staticmethod
    def validate_balance(balance):
        return balance >= 1000

acc1 = BankAccount(3906981914, "Khushi", 8000)

acc1.display()
acc1.deposit(2000)
acc1.withdraw(3000)
acc1.display()
