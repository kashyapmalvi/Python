class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        # Private attribute: cannot be accessed directly outside the class
        self.__balance = initial_balance 

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Invalid deposit amount.")

    # Public method to withdraw money (includes validation)
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds or invalid amount.")

    # Getter method to safely view the balance
    def get_balance(self):
        return f"Current Balance: ${self.__balance}"

# --- Using the class ---
account = BankAccount("Alex", 1000)

# 1. Accessing public data works fine
print(account.account_holder) # Output: Alex

# 2. Accessing private data directly will fail
# print(account.__balance)    # This would raise an AttributeError

# 3. Interacting via public methods (The "Proper" way)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())   # Output: Current Balance: $1300