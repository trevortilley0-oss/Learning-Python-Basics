def checkBalance(b):
    print(f"Currenct balance: ${b}")

def deposit(b, a):
    if a > 0:
        b = b+a
        print(f"Deposited: ${a} New balance is ${b}")
    else:
        print("Invalid deposit amount!")

        return b

def withdraw(b, a):
    if a > 0:
        if a <= b:
            b = b - a
            print(f"Withdrawal: ${a} New balance is ${b}")
        else:
            print("Insufficient funds")
    else: print("Did not enter vaslid amount")
    return b

#define balance, give user menu - exit
def atm():
    balance = 1042.50

    while True:
        print("\nWelcome to the ATM")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = int(input("CHoose an option:"))

        if choice == 1:
            checkBalance(balance)
        elif choice == 2:
            amount = float(input("Enter deposit amount: "))
            balance = deposit(balance, amount)
        elif choice == 3:
            amount = float(input("Enter withdrawal amount: "))
            balance = withdraw(balance, amount)
        elif choice == 4:
            print("Thank you for using the ATM Machine!")
            break
        else:
            print("Invalid option. Please try again.")


atm()