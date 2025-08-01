from datetime import datetime

# now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
balance = 1000
transactions_history = []


def checkbalance():
    global balance
    print(f"Your current balance is :{balance}.Rs")


def deposit():

    global balance
    global transactions_history
    amount = int(input("Enter amount to deposit : "))
    if amount > 0:
        balance += amount
        now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print(f"Rs {amount} deposited is added in your account.")
        transactions_history.append(f"{now} Deposited: Rs {amount}")
    else:
        print("Invalid amount, Please re-enter the  amount.")


def withdraw():
    global balance
    global transactions_history
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    amount = int(input("Enter here your amount: "))
    if amount > 0 and amount <= balance:
        balance -= amount
        transactions_history.append(f"{now} Withdraw: Rs {amount}")
    else:
        print("Insufficient amount!, please try again! ")


print("\n")
while True:
    print("\n")
    print("Welcome to the ATM")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw money")
    print("4. Transaction History")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        checkbalance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        print("Transaction History:")
        for transaction in transactions_history:
            print(transaction)
    elif choice == 5:
        print("Thankyou, Exiting ATM.....")
        break
    else:
        print("Invalid choice, Please try again.")
