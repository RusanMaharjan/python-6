import random
from ErrorHandling import AmountDepositError, AmountWithdrawError

class Bank:
    def __init__(self, account_name, initial_balance):
        self.account_name = account_name
        self.initial_balance = initial_balance
        self.account_number = "".join(str(random.randint(0, 9)) for i in range(16))

    # deposit function
    def deposit(self, amount):
        if amount > 100:
            self.initial_balance += amount
            print('\n')
            print('-'*100)
            print(f'Rs.{amount} has been deposited to A/C no. {self.account_number}.')
            print('-'*100)
        else:
            raise AmountDepositError('Error: Deposit amount must be more than Rs.100.')

    # Withdraw Function
    def withdraw(self, amount):
        if amount < self.initial_balance:
            self.initial_balance -= amount
            print('\n')
            print('-'*100)
            print(f'Rs.{amount} has been withdrawn from A/C no. {self.account_number}.')
            print('-'*100)
        else:
            raise AmountWithdrawError('Error: Withdraw amount must be less than balance amount.')

    # Show Detail Function
    def show_details(self):
        print('\n')
        print('-'*100)
        print('Bank Details')
        print('-'*50)
        print(f'Account Name: {self.account_name}')
        print(f'Initial Balance: {self.initial_balance}')
        print(f'Account Number: {self.account_number}')
        print('-'*100)