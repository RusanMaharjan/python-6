from Bank import Bank
from Storage import all_accounts
from Functions import findAccountByAccountNumber, depositAmount, withdrawAmount


def application():
    while True:
        print('\n')
        print('Welcome to Bank Application')
        print('1. Create Account')
        print('2. Deposit Balance')
        print('3. Withdraw Balance')
        print('4. Show Details')
        print('5. Exit')

        choice = int(input('Enter your choice (1 - 5):'))

        # for creating account
        if choice == 1:
            y_n = input('Do you really want to create new account (y/n)? ')
            if y_n == 'y':
                name = input('Enter your name: ')
                balance = int(input('Enter your initital balance to deposit to account: '))
                
                if balance > 100:
                    b = Bank(name, balance)
                    all_accounts.append(b)
                    print('\n')
                    print('-'*100)
                    print(f'Account created of name {name} with balance Rs.{balance} and A/C no. {b.account_number}. ')
                    print('-'*100)
                else:
                    print('\n')
                    print('-'*100)
                    print('Error: Initital balance must be more than Rs.100.')
                    print('-'*100)
            else:
                print('-'*100)
                print('Continue with your transaction.')
                print('-'*100)

        elif choice in [2, 3, 4]:
            acc_number = input('Enter your account number: ')
            find_acc = findAccountByAccountNumber(acc_number)
            if find_acc:
                # for deposit balance
                if choice == 2:
                    y_n = input('Do you really want to deposit balance (y/n)? ')
                    if y_n == 'y':
                        depositAmount(find_acc)
                    else:
                        print('\n')
                        print('-'*100)
                        print('Continue with your transaction.')
                        print('-'*100)

                # for withdraw balance
                elif choice == 3:
                    y_n = input('Do you really want to withdraw balance (y/n)? ')
                    if y_n == 'y':
                        withdrawAmount(find_acc)
                    else:
                        print('\n')
                        print('-'*100)
                        print('Continue with your transaction.')
                        print('-'*100)
                    
                # for show details
                elif choice == 4:
                    y_n = input('Do you really want to show your bank details (y/n)? ')
                    if y_n == 'y':
                        find_acc.show_details()
                    else:
                        print('\n')
                        print('-'*100)
                        print('Continue with your transaction.')
                        print('-'*100)
            else:
                print('\n')
                print('-'*100)
                print('Error: No account found with given account number.')
                print('-'*100)
                
        elif choice == 5:
            print('\n')
            print('-'*100)
            print('Thank you for choosing us.')
            print('-'*100)
            break
        else:
            print('\n')
            print('-'*100)
            print('Error: Invalid Input. Enter valid input from 1 to 5.')
            print('-'*100)