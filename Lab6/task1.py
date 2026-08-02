class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")


# Driver Code
account = BankAccount("123456789", 5000, "02-08-2026", "Fahim")

account.check_balance()
account.deposit(2000)
account.withdraw(1500)
account.check_balance()
