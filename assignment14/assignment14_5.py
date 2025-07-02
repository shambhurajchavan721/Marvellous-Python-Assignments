class BankAccount:
    def _init_(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawn {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdraw amount must be positive.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Balance: {self.balance}")


def main():
    account = BankAccount(12345, "Rohit", 1000)
    account.display_balance()
    account.deposit(500)
    account.withdraw(300)
    account.withdraw(1500)
    account.display_balance()


if __name__ == "__main__":
    main()