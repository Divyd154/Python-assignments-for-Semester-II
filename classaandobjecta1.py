class BankAcc:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def check_balance(self):
        print("Current Balance:", self.balance)

    def display_account(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


b1 = BankAcc("123456789", 1000)

b1.display_account()
b1.deposit(500)
b1.withdraw(200)
b1.check_balance()

