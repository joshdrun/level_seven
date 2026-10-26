from bankfunctions import withdraw



has_error = True
while has_error:
    try:    
        # Your code here
        number = int(input("Enter a number: "))
        print(f"You entered the number: {number}")
        has_error = False
    except ValueError:
        print("invalid input")
        has_error = True
    except KeyboardInterrupt:
        print("Keyboard interrupt detected")
        has_error = True
    except:
        print("An unexpected error occurred")
        has_error = True
    else:
        print("No error occurred")
        has_error = False
        continue
    finally:
        print("This block always executes")






    balance = 1000  # Example initial balance
    try:
        amount = int(input("Enter the amount to withdraw: "))
    except ValueError:
        print("Invalid input for withdrawal amount")
        amount = 0  # Set a default value to avoid further errors
    except InsufficientFunds:
        print("Insufficient funds for withdrawal")
        amount = 0  # Set a default value to avoid further errors
    else:
        balance = withdraw(amount, balance)
        print(f"Remaining balance: {balance}")