# Create a class called BankAccount that has private attribute balance (optional: default 0) and public attribute owner. It should have method deposit that only accepts positive number & adds to user’s balance. Add another method withdraw that accepts positive number and withdraws from account. After withdraw display the remaining amount or message insufficient balance. Create property attribute balance to display it. Create method called transfer that transfer balance from one account to another. Initialize two bankaccount to show demo.


class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = balance  # Private attribute

    @property
    def balance(self):
        """Property to get the current balance"""
        return self._balance

    def deposit(self, amount):
        """Deposit money into the account"""
        if amount <= 0:
            print("Deposit amount must be positive")
            return False
        self._balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")
        return True

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return False
        if amount > self._balance:
            print("Insufficient balance")
            return False
        self._balance -= amount
        print(f"Withdrew ${amount:.2f}. Remaining balance: ${self._balance:.2f}")
        return True

    def transfer(self, other_account, amount):
        """Transfer money to another account"""
        if amount <= 0:
            print("Transfer amount must be positive")
            return False
        if amount > self._balance:
            print("Insufficient balance for transfer")
            return False
        self._balance -= amount
        other_account._balance += amount
        print(f"Transferred ${amount:.2f} to {other_account.owner}")
        print(f"Your new balance: ${self._balance:.2f}")
        return True

    def __str__(self):
        return f"BankAccount(owner='{self.owner}', balance=${self._balance:.2f})"


# Demonstration
if __name__ == "__main__":
    print("Creating two bank accounts:")
    account1 = BankAccount("Alice", 1000.0)
    account2 = BankAccount("Bob", 500.0)
    print(account1)
    print(account2)

    print("\nTesting deposits:")
    account1.deposit(200.0)
    account2.deposit(-100.0)  # Should fail

    print("\nTesting withdrawals:")
    account1.withdraw(300.0)
    account1.withdraw(2000.0)  # Should fail (insufficient balance)
    account2.withdraw(0.0)  # Should fail (non-positive amount)

    print("\nTesting transfer:")
    account1.transfer(account2, 400.0)
    account1.transfer(account2, 1000.0)  # Should fail (insufficient balance)

    print("\nFinal balances:")
    print(f"{account1.owner}'s balance: ${account1.balance:.2f}")
    print(f"{account2.owner}'s balance: ${account2.balance:.2f}")
