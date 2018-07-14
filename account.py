class Account:

    def __init__(self, amount, id):
        self.amount = amount
        self.id = id

    def set_amount(self, new_amount):
        self.amount = new_amount

    def get_amount(self):
        return self.amount