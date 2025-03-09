balance = 5000
a = False

while a != True:
    print("""
    -Welcome to 'Bank Tracker'-
    To start, choose an option: 
    1: Withdraw Cash
    2: Deposit Cash
    3: Check Balance
    4: Quit App""")
    option = input("Choose an option: ")
    if option = 1:
        withdrawAmount = input("Choose how much you wish to withdraw: ")
        if withdrawAmount <= 0 or withdrawAmount > balance:
            print("Sorry, you have given an invalid number. Try again.")
        else:
            balance -= withdrawAmount
            print(f"Transaction Complete! Total: {balance}")