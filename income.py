from trasaction import Transaction

class Income(Transaction):
    def __init__(self, amount, category, date, source):
        super().__init__(amount, category,  date)
        self.source = source

    def display_transaction(self):
        return f'Income: {self.amount}, Category: {self.category}, Date: {self.date}, Source: {self.source}'