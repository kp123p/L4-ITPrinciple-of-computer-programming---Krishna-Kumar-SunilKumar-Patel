from abc import ABC, abstractmethod
class Transaction(ABC):
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

    @abstractmethod
    def display_transaction(self):
        pass