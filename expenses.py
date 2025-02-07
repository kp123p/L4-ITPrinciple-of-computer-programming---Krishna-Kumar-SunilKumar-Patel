from trasaction import Transaction

class Expense(Transaction):
    def __init__(self, amount, category, date, necessity):
        super().__init__(amount, category, date)
        self.necessity = necessity

    def display_transaction(self):
        return f'Expense: {self.amount}, Category: {self.category} Date: {self.date}, Necessity: {self.necessity}'