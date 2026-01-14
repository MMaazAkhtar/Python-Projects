class Bank_Account:
    def __init__(self,account_number,account_holder,balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self,amount):
        return f"Balance:{self.balance + amount}"
    def withdrawal(self,amount):
        return f"Balance left:{self.balance - amount}" if amount<self.balance else ("Not enough money! ")
    def get_balance(self):
        return f"Balance:{self.balance}"
    def display_account_info(self):
        return f"Account Number:{self.account_number}\nAccount Holder:{self.account_holder}\nCurrent Balance:{self.balance}\n"

user_input=input("Select the Operation:1)Deposit\n2)Withdrawal\n3)Check Balance\n4)Display Account Details\nType number: ")
Account_Number=int(input('Enter Account Number: '))
Account_Holder=input('Enter your Name: ')
Balance=int(input('Enter Balance: '))
person1=Bank_Account(Account_Number,Account_Holder,Balance)
match user_input:
    case "1":
        amount=int(input('Enter the amount you want to deposit: '))
        d=person1.deposit(amount)
        print(d)
    case "2":
        amount=int(input('Enter the amount you want to withdraw: '))
        d=person1.withdrawal(amount)
        print(d)
    case "3":
        d=person1.get_balance()
    case "4":
        d=person1.display_account_info()
    case _:
        print("Invalid Input")



