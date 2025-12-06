'''1. Create a Python Class to Simulate a Bank Account

Goal: Master OOP (Object-Oriented Programming) – essential for structuring IoT systems and ML pipelines.

✅ What to include:

Attributes: account_holder, balance

Methods: deposit(amount), withdraw(amount), check_balance()

Use constructor (__init__)

Add validation (prevent negative balance)

📌 Why important:
IoT gateways and ML models use class structures to manage device states and ML models.'''
from os import access

class account_holder:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def withdraw(self,amount):
        self.balance -= amount
        print("Withdrew : $", amount)

    def deposit(self,amount):
        self.balance += amount
        print("Deposited : $", amount)

    def check_balance(self):
        print(f"Your current balance is ${self.balance}")

name = input("Enter account holder name: ")
balance = float(input("Enter balance: "))

while balance < 0:
        print("Balance cannot be negative")
        balance = float(input("Enter balance: "))

account = account_holder(name, balance)
while True:
    n = int(input("Choose an option: \n1. Deposit \n2. Withdraw \n3. Check Balance \n4.exit\n :"))
    if n == 1:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif n == 2:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif n == 3:
        account.check_balance()
    else:
        break