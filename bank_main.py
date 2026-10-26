from bankfunctions import BankAccount
import random



active = True

name_user = input("Enter your name: ")
my_account = BankAccount(0)
account_number = random.randint(10000000, 99999999)

while active:
    print("1. View Account Info")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Quit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print(f"Account Information for {name_user}:")
        print(f"Account Number: {account_number}")
        my_account.view_account_info()
    elif choice == "2":
        try:
            amount = float(input("Enter amount to deposit: "))
        except ValueError:
            print("Please enter a valid number.")
        else:
            my_account.deposit(amount)
            print(f"Account balance: ${my_account.balance:,.2f}")
    elif choice == "3":
        run_again = True
        while run_again:
            try:
                amount = float(input("Enter amount to withdraw: "))
                my_account.withdraw(amount)
                print(f"Account balance: ${my_account.balance:,.2f}")
                run_again = False
            except:
                print("Please enter a valid number within your available balance.")
                run_again = True
                pass
    elif choice == "4":
        my_account.quit()
        active = False
    else:
        print("Invalid choice. Please try again.")



