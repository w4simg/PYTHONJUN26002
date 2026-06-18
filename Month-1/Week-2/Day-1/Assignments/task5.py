# Task 5: Create a Bank Account Class
# Requirements:
# - Create a class named BankAccount.
# - Use a constructor.
# - Store: account holder name, account number, balance.
# - Create a method to display account details.

class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def display_details(self):
        print("Bank Account Details:")
        print("Account Holder Name:", self.name)
        print("Account Number:", self.account_number)
        print("Balance: Rs.", self.balance)

# Create object
account = BankAccount("Rohit Sharma", "9876543210", 250000)

# Display details
account.display_details()
