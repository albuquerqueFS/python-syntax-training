class BankAccount(object):
    '''edsaf fasfgsa'''
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def overdraw(self):
        return self.balance < 0
my_account = BankAccount(15)
my_account.withdraw(50)
print(my_account.balance, my_account.overdraw())