from bank_account import BankAccount

account1 = BankAccount(1234567)
account2 = BankAccount(7654321, 150.00)
account3 = BankAccount(3232323, 584.73)

print(account1)
print(account2)
print(account3)
print()

account1.deposit(28.61)
account2.withdraw(40.00)
account3.deposit(1200)
account3.withdraw(200)