from Storage import all_accounts
from ErrorHandling import AmountDepositError, AmountWithdrawError

# Search account by account number function
def findAccountByAccountNumber(acc_number):
    for account in all_accounts:
        if acc_number == account.account_number:
            return account
    return None

# Deposit amount function after finding account
def depositAmount(obj):
    balance = int(input('Enter your deposit balance amount: '))
    try:
        obj.deposit(balance)
    except AmountDepositError as e:
        print(e)

# Withdraw amount function after finding account
def withdrawAmount(obj):
    balance = int(input('Enter your withdraw balance amount: '))
    try:
        obj.withdraw(balance)
    except AmountWithdrawError as e:
        print(e)