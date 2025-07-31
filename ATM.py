balance = 1000
def checkbalance():
    global balance
    print(f"Your current balance is {balance}.Rs")
def deposit():
    global balance
    amount = int(input("Enter amount to deposit : "))
    if amount > 0:
        balance += amount
        print(f"Rs {amount} deposited is added in your account.")
        checkbalance()
    else:
         print("Invalid amount, Please retry.")
def withdraw():
    global balance 
    amount = int (input("Enter withdrawal amount : "))
    if amount < balance :
        balance -= amount
        print(f"Rs {amount} withdrawn from your account.")
        checkbalance()
    elif amount > balance:
        print("Insufficient balance.")
    else:
        print("Invalid amount, Please retry.")



# Main functions 
while True:
    print("=========WELCOME TO ATM=========")
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        checkbalance()
    elif choice == 2:
        deposit()
    elif choice == 3 :
        withdraw()
    elif choice == 4:
        print("Thankyou , Exiting ATM.....")
        break
    else:
        print("Invalid choice, Please try again.")
    
