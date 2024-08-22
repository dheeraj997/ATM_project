import random

class Account:
    def __init__(self, balance=0, accountNumber=-1):
        self.balance = float(balance)
        if accountNumber == -1:
            self.accountNumber = random.randint(10000000, 99999999)
        else:
            self.accountNumber = int(accountNumber)
        self.transLog = []

    def getAccountNumber(self):
        return self.accountNumber

    def getBalance(self):
        return self.balance

    def getTransactions(self):
        return self.transLog

    def deposit(self, amount):
        self.balance += amount
        self.addTransaction(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the transaction")
        else:
            self.balance -= amount
            self.addTransaction(f"Withdrew {amount}")

    def addTransaction(self, transaction):
        self.transLog.append(transaction)


class Customer(Account):
    def __init__(self,name,balance,accountNumber=-1):
        super().__init__(balance,accountNumber)
        self.name=name
        self.createPin()

    def createPin(self):
        self.pin=random.randint(1000,9999)
    
    def getName(self):
        return self.name
    
    def getPin(self):
        return self.pin
from datetime import datetime
 
class ATM:
    def __init__(self,accounts_file="accounts.txt"):
        self.accounts=[]
        try:
            with open(accounts_file,'r') as file:
                next(file)
                for line in file:
                
                    accountNumber,name,balance,fakepin=line.strip().split(",")

                    user=Customer(name=name,balance=float(balance),accountNumber=int(accountNumber))

                    self.accounts.append(user)

                    print(f"New account created for {name} with PIN {user.getPin()}")
                self.authorize()
        except Exception as e:
            print(f"error in the account {e}")
        
    def authorize(self):
        invalid_attempts = 0
        while invalid_attempts < 3:
            try:
                entered_pin = int(input("Enter your PIN: "))
                user = self.findUserByPin(entered_pin)
                if user:
                    self.displayMenu(user)
                    return
                else:
                    invalid_attempts += 1
                    print("Invalid PIN, try again.")
            except ValueError:
                invalid_attempts += 1
                print("Invalid PIN, try again.")
        print("You have performed too many invalid logins, Goodbye")

    def findUserByPin(self, entered_pin):
        for user in self.accounts:
            if user.getPin() == entered_pin:
                return user
        return None

    def displayMenu(self, user):
        while True:
            print(f"\nWelcome {user.getName()}")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Balance")
            print("4. Account Info")
            print("5. Quit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.deposit(user)
            elif choice == '2':
                self.withdraw(user)
            elif choice == '3':
                self.balance(user)
            elif choice == '4':
                self.accountInfo(user)
            elif choice == '5':
                if self.exit(user):
                    break
            else:
                print("Invalid choice, try again.")

    def deposit(self, user):
        while True:
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount < 0:
                    print("Negative amount. Try again.")
                else:
                    user.deposit(amount)
                    print(f"{amount} deposited successfully.")
                    break
            except ValueError:
                print("Invalid amount. Use digits only.")

    def withdraw(self, user):
        while True:
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount < 0:
                    print("Negative amount. Try again.")
                elif amount > user.getBalance():
                    print("Insufficient funds to complete the transaction.")
                else:
                    user.withdraw(amount)
                    print(f"{amount} withdrawn successfully.")
                    break
            except ValueError:
                print("Invalid amount. Use digits only.")

    def balance(self, user):
        print(f"Current balance: {user.getBalance()}")
        user.addTransaction("Checked balance")

    def accountInfo(self, user):
        print(f"Account Number: {user.getAccountNumber()}")
        print(f"Account Balance: {user.getBalance()}")
        print(f"Account Holder: {user.getName()}")

    def exit(self, user):
        confirm = input("Are you sure you want to exit? (Y/N): ").strip().lower()
        if confirm == 'y':
            print("\nReceipt:")
            print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Account Holder: {user.getName()}")
            print(f"Remaining Balance: {user.getBalance()}")
            print("Transactions:")
            for transaction in user.getTransactions():
                print(f" - {transaction}")
            return True
        return False





                    