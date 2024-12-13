class BankAccount:
     def __init__(self, account_number, balance):
         self.__account_number = account_number
         self.__balance = balance
     def deposit(self, amount):
         if amount > 0:
            self.__balance += amount
         else:
          print("Invalid deposit amount.")
         
     def withdraw(self, amount):
        if amount > 0 and amount <=self.__balance:
            self.__balance -= amount
        else:
         print("Invalid withdrawal amount.")
         
     def display_account_info(self):
         print(f"Account Number: {self.__account_number}")
         print(f"Current Balance: {self.__balance}")
       
     def get_account_number(self):
         return self.__account_number
         
     def get_balance(self):
         self.display_balance()
         
     def set_balance(self, balance):
        if balance >= 0:
             self.__balance = balance
        else:
         print("Invalid balance.")
         
     def display_balance(self):
         print(f"Current Balance: {self.__balance}")
         
#Test the BankAccount class
account = BankAccount("123456789", 2000.00)
account.display_account_info()
account.deposit(float(input("Add Amount: ")))
account.display_account_info()
account.withdraw(float(input("Deduct Amount: ")))
account.display_account_info()
account.set_balance(float(input("Set Balance: ")))
account.display_account_info()