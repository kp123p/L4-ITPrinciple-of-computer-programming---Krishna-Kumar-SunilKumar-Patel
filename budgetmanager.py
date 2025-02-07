class BudgetManager:
    def __init__(self):
        self.income_list = []
        self.expense_list = []
        self.budget_limit = 0

    def set_budget_limit(self, limit):
        self.budget_limit = limit
        print(f"Budget limit set to {limit}")

    def add_income(self, income):
        self.income_list.append(income)
        print(f"Income added: {income.display_transaction()}")

    def add_expense(self, expense):
        self.expense_list.append(expense)
        print(f"Expense added: {expense.display_transaction()}")

    def calculate_balance(self):
        total_income = sum(income.amount for income in self.income_list)
        total_expenses = sum(expense.amount for expense in self.expense_list)
        return total_income - total_expenses

    def generate_report(self):
        total_income = sum(income.amount for income in self.income_list)
        total_expenses = sum(expense.amount for expense in self.expense_list)
        balance = self.calculate_balance()
        print(f"Total Income: {total_income}, Total Expenses: {total_expenses}, Balance: {balance}")

    def send_alerts(self):
        total_expenses = sum(expense.amount for expense in self.expense_list)
        if total_expenses > self.budget_limit:
            print("Alert: You have exceeded your budget limit!")
