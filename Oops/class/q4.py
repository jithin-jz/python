# 🔹 4. Bank Account

# Create a class BankAccount with attributes owner and balance (default = 0).

# Methods: deposit(amount), withdraw(amount), and check_balance().

# Ensure withdrawal cannot happen if balance is insufficient.

class BankAccount:

    def __init__(self,owner:str,balance:float = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount:float):
        self.balance += amount
        print(f'Deposited {amount}.New balance:{self.balance}')

    def withdraw(self,amount:float):
        if amount > self.balance:
            print('Insufficent balance')
        else:
            self.balance -= amount
            print(f'Withdrew {amount}.New balance:{self.balance}')
            
    def current_balance(self)->float:
        return self.balance
    
    def __str__(self) -> str:
        return f'Owner:{self.owner} Balance:{self.balance}'
    
user1 = BankAccount('Anand')
user1.deposit(1000)
user1.withdraw(10)

print(user1)
