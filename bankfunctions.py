class BankAccount:



    def __init__(self, balance):
        self.balance = balance
        

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds, try again")
            raise ValueError("The provided value is invalid.")
            

        self.balance -= amount
        return self.balance
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def view_account_info(self):
        
        print(f"Account balance: {self.balance}")

    def quit(self):
        print("Exiting the program.")
        exit()
