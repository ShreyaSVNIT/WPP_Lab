class BankAccount:
    def __init__(self, account_number, customer_name, balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def display(self):
        print(f"\nAccount Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: ₹{self.balance}\n")


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self):
        account_number = input("Enter account number: ")
        customer_name = input("Enter customer name: ")
        initial_deposit = float(input("Enter initial deposit amount: "))
        if account_number in self.accounts:
            print("Account number already exists.")
        else:
            self.accounts[account_number] = BankAccount(account_number, customer_name, initial_deposit)
            print(f"Account for {customer_name} created successfully with balance ₹{initial_deposit}.")

    def deposit(self):
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self):
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def display_account(self):
        account_number = input("Enter account number: ")
        account = self.accounts.get(account_number)
        if account:
            account.display()
        else:
            print("Account not found.")


bank = Bank("TechBank")

while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Account")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        bank.create_account()
    elif choice == "2":
        bank.deposit()
    elif choice == "3":
        bank.withdraw()
    elif choice == "4":
        bank.display_account()
    elif choice == "5":
        print("Exiting the system. Thank you for using TechBank!")
        break
    else:
        print("Invalid choice! Please try again.")
