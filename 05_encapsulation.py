# private double underscore
class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder  # Public attribute
        self._balance = initial_balance       # Protected attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):  # Public method to access protected attribute
        return f"Balance: {self._balance}"

# Creating an object
account = BankAccount("Alice", 1000)

# Accessing public attribute
print(account.account_holder)  # Output: Alice

# Accessing balance through public method (encapsulation in action)
print(account.get_balance())  # Output: Balance: 1000

# Depositing money
account.deposit(500)
print(account.get_balance())  # Output: Balance: 1500

# Withdrawing money
account.withdraw(200)
print(account.get_balance())  # Output: Balance: 1300


# example 2 private attributes 

class SecureAccount:
    def __init__(self, owner, balance):
        self.__owner = owner        # Private attribute
        self.__balance = balance    # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

# Creating an object
secure_account = SecureAccount("Bob", 500)

# Accessing private attributes directly (will cause an error)
# print(secure_account.__balance)  # AttributeError

# Accessing private attributes through methods
print(secure_account.get_balance())  # Output: 500
