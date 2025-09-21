from accounts import account, create_account, user_account

print("Welcome to the Banking App")

while user_account is None:
    user_account = create_account()

print("what would you like to do?")
while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("Enter your choice (1-4): ")
    choice = input()
    
    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        print(user_account.deposit(amount))
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        print(user_account.withdraw(amount))
    elif choice == '3':
        print(f"Current balance: {user_account.get_balance()}")
    elif choice == '4':
        print("Thank you for using the Banking App. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")