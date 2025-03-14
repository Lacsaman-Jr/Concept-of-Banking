TERMINATE, WITHDRAW, DEPOSIT, BALANCE, SUMMARY, WITHDRAW_SUMMARY = (0, 1 , 2, 3, 4, 5)

class BankAccount:
    def __init__(self, accountName):
        self.name = accountName
        
    __accountBalance = 0
    __transactions = []

    def depositAmount(self):
        deposit = float(input('Enter amount to deposit:'))
        if deposit <= 0:
            print('Invalid amount')
        else:
            self.__accountBalance += deposit
            self.__transactions.append(('deposit', deposit))
        
    def withdrawAmount(self):
        withdraw = float(input('Enter amount to withdraw:'))
        if withdraw > self.__accountBalance:
            print('Invalid amount')
        else:
            self.__accountBalance -= withdraw
            self.__transactions.append(('withdraw', withdraw))
    def checkBalance(self):
        print(f'Your present balance is: P {self.__accountBalance}')
        self.__transactions.append(('check-balance', self.__accountBalance))

    def printTransactions(self, operations):
      
        lines = map(lambda trans: f'{trans[0]} = {trans[1]}', operations)
        counter = 1
        for line in lines:
            print(f'{counter}: {line}')
            counter += 1
            
    def printSummary(self):
        self.printTransactions(self.__transactions)
    
    def printWithdrawSummary(self):
        self.withdraws = filter(lambda trans: trans[0] == 'withdraw' , self.__transactions )
        self.printTransactions(self.withdraws)

def printMenu():
    print(f"\tEnter {WITHDRAW}: withdraw")
    print(f"\tEnter {DEPOSIT}: deposit")
    print(f"\tEnter {BALANCE}: check balance")
    print(f"\tEnter {SUMMARY}: summary of transactions")
    print(f"\tEnter {WITHDRAW_SUMMARY}: summary of withdraws")
    print(f"\tEnter {TERMINATE}: exit")


def main():
    account = BankAccount ("lacsaman")
    operation = BALANCE
    while operation != TERMINATE:
        printMenu()
        operation = int(input("Enter op code: "))
        if operation == WITHDRAW:
            account.withdrawAmount()
        elif operation == DEPOSIT:
            account.depositAmount()
        elif operation == BALANCE:
            account.checkBalance()
        elif operation == SUMMARY:
            account.printSummary()
        elif operation == WITHDRAW_SUMMARY:
            account.printWithdrawSummary()
        elif operation == TERMINATE:
            print('Good bye')
        else:
            print("Invalid operation")
            
if __name__ == '__main__':
    main()
