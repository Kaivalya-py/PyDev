#  Create a Python program that simulates a bank account system. The base class `Account` should have attributes like `account_number`, `account_name`, and `balance`. It should include deposit and withdraw methods that update the balance accordingly. Derive two subclasses from `Account`: `SavingsAccount` and `CheckingAccount`. Add a unique feature to each subclass, such as a `minimum_balance` requirement for `SavingsAccount` and a `write_check()` method for `CheckingAccount`. Ensure proper usage of inheritance and encapsulation principles.

class Account:
    def __init__(self, account_number, account_name, balance):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

class SavingsAccount(Account):
    def __init__(self, account_number, account_name, balance, minimum_balance):
        super().__init__(account_number, account_name, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print("Withdrawal failed. Minimum balance requirement not met.")
        else:
            super().withdraw(amount)

class CheckingAccount(Account):
    def write_check(self, amount):
        self.withdraw(amount)

s = SavingsAccount(123, "John Doe", 1000, 500)

s.deposit(500)
print(s.balance)
s.withdraw(200)
print(s.balance)
c = CheckingAccount(456, "Jane Doe", 2000)
c.deposit(1000)
print(c.balance)
c.write_check(500)
print(c.balance)