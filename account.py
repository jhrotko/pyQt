class Account:

    def __init__(self, amount, id):
        self.amount = amount
        self.id = str(id)

    def set_amount(self, new_amount):
        self.amount = new_amount