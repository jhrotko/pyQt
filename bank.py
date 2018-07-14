
from account import Account


class Bank:

    def __init__(self):
        self.total_account = 0
        self.accounts = list()

    def add_account(self, account):
        self.accounts.append(account)
        self.total_account += 1

    def create_account(self, amount):
        acount = Account(amount, self.total_account)
        self.accounts.append(acount)