# 5. Banking System

# Parent:

# BankAccount

# Child:

# SavingsAccount
# CurrentAccount

# Implement withdrawal rules.

class BankAccount:
    def withdrawalRules(self):
        pass
    
class SavingsAccount(BankAccount):
    def withdrawalRules(self, balance, amount):
        if balance - amount >= 5000:
            print("Withdrawal successful")
        else:
            print("Must have 4000 rupees in your bank account ")
        
class CurrentAccount(BankAccount):
    def withdrawalRules(self, balance ,amount):
        if balance - amount >= 2000:

            print("Withdrawal Successfull")
        else:
            print("Must have 2000 rupees in your bank account")

savingsAccount = SavingsAccount()
savingsAccount.withdrawalRules(1000,3000)

currentAccount = CurrentAccount()
currentAccount.withdrawalRules(6000,3500)