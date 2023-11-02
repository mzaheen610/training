class Bank:

    def __init__(self) -> None:
        self.accountNumber = 0
        self.currentBalance = 0
        self.branchName = 'Default'
    def deposit(self,amount):
        self.currentBalance += amount
        print(f"Your account {self.accountNumber} has been deposited with {amount} $",)
    
    def withdraw(self,amount):
        self.currentBalance -= amount
        print(f"{amount} withdrawn from your account {self.accountNumber}.")
    
    def checkBalance(self):
        print("Current balance is: ", self.currentBalance)

newAccount = Bank()
newAccount.deposit(20000)
newAccount.checkBalance()
newAccount.withdraw(5000)
newAccount.checkBalance()
