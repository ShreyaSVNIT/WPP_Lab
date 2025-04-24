class BankAcct:
    def __init__(self, number, name, bal=0.0):
        self.acctnum = number
        self.custname = name
        self.balance = bal

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Balance insufficient"

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def display(self):
        print(f"\nAccount Number: {self.acctnum}")
        print(f"Customer Name: {self.custname}")
        print(f"Account Balance: ₹{self.balance:.2f}\n")

number = int(input("Enter account number: "))
name = input("Enter customer name: ")
bal = float(input("Enter initial balance: "))

acct1 = BankAcct(number, name, bal)
acct1.display()

deposit_amount = float(input("Enter amount to be deposited: "))
acct1.deposit(deposit_amount)

withdraw_amount = float(input("Enter amount to be withdrawn: "))
print(acct1.withdraw(withdraw_amount))

acct1.display()
