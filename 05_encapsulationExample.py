class BankAccount:
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder  # Private attribute
        if not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("Balance must be a non-negative number.")
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.__balance += amount  # Add amount to balance

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")  # Check for sufficient balance
        self.__balance -= amount  # Deduct amount from balance

    def get_balance(self):
        return f"Current balance is: {self.__balance:.2f}"  # Format balance to 2 decimals

    def get_account_holder(self):
        return f"Account holder name is: {self.__account_holder}"


# Test Cases
try:
    obj1 = BankAccount("Rishabh", 0)
    print(obj1.get_account_holder())
    print(obj1.get_balance())

    # Valid deposit
    obj1.deposit(1000)
    print(obj1.get_balance())

    # Valid withdrawal
    obj1.withdraw(750.8)
    print(obj1.get_balance())

    # Invalid deposit
    try:
        obj1.deposit(-200)
    except ValueError as e:
        print(f"Error during deposit: {e}")

    # Invalid withdrawal
    try:
        obj1.withdraw(5000)
    except ValueError as e:
        print(f"Error during withdrawal: {e}")

except ValueError as e:
    print(f"Initialization Error: {e}")
