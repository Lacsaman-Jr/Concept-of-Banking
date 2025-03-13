TERMINATE, WITHDRAW, DEPOSIT, BALANCE, SUMMARY, WITHDRAW_SUMMARY = (0, 1 , 2, 3, 4, 5)

accountBalance = 0
transactions = []

def printMenu():
    print(f"\tEnter {WITHDRAW}: withdraw")
    print(f"\tEnter {DEPOSIT}: deposit")
    print(f"\tEnter {BALANCE}: check balance")
    print(f"\tEnter {SUMMARY}: summary of transactions")
    print(f"\tEnter {WITHDRAW_SUMMARY}: summary of withdraws")
    print(f"\tEnter {TERMINATE}: exit")

def withdrawAmount():
    global accountBalance
    withdraw = float(input('Enter amount to withdraw:'))
    if withdraw > accountBalance:
        print('Invalid amount')
    else:
        accountBalance -= withdraw
        transactions.append(('withdraw', withdraw))

def depositAmount():
    global accountBalance
    deposit = float(input('Enter amount to deposit:'))
    if deposit <= 0:
        print('Invalid amount')
    else:
        accountBalance += deposit
        transactions.append(('deposit', deposit))

def checkBalance():
    print(f'Your present balance is: P {accountBalance}')
    transactions.append(('check-balance', accountBalance))

def printTransactions(operations):
    lines = map(lambda trans: f'{trans[0]} = {trans[1]}', operations)
    counter = 1
    for line in lines:
        print(f'{counter}: {line}')
        counter += 1

def printSummary():
    printTransactions(transactions)

def printWithdrawSummary():
    withdraws = filter(lambda trans: trans[0] == 'withdraw' , transactions )
    printTransactions(withdraws)

def main():
    operation = BALANCE
    while operation != TERMINATE:
        printMenu()
        operation = int(input("Enter op code: "))
        if operation == WITHDRAW:
            withdrawAmount()
        elif operation == DEPOSIT:
            depositAmount()
        elif operation == BALANCE:
            checkBalance()
        elif operation == SUMMARY:
            printSummary()
        elif operation == WITHDRAW_SUMMARY:
            printWithdrawSummary()
        elif operation == TERMINATE:
            print('Good bye')
        else:
            print("Invalid operation")

main()
