user_account = None

class account():
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"New balance after deposit: {self.balance}"
        return "Invalid Deposit Amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"New balance after withdrawal: {self.balance}"
        return "Funds Unavailable"
    
    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f"Account {self.account_number} held by {self.account_holder} has balance: {self.balance}"

def create_account():
    global user_account
    print("Create a new account")
    print("Enter Account Number:")
    account_number = input()
    print("Enter Account Holder Name:")
    account_holder = input()
    user_account = account(account_number, account_holder)
    print("Account created successfully!")
    return user_account