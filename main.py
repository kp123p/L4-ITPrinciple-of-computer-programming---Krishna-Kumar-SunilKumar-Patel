from user import User
from income import Income
from expenses import Expense
from budgetmanager import BudgetManager

def main():
    print("Welcome to the Personal Budget Manager!")

    username = input("Enter your username: ")
    password = input("Enter your password: ")
    email = input("Enter your email: ")

    user = User(username, password, email)
    user.register(username, password, email)

    if not user.login(username, password):
        return

    budget_manager = BudgetManager()
    budget_limit = float(input("Set your monthly budget limit: "))
    budget_manager.set_budget_limit(budget_limit)

    while True:
        choice = input("Do you want to add an income or an expense? (income/expense/exit): ").lower()

        if choice == "income":
            amount = float(input("Enter income amount: "))
            category = input("Enter income category: ")
            date = input("Enter income date (YYYY-MM-DD): ")
            source = input("Enter income source: ")
            income = Income(amount, category, date, source)
            budget_manager.add_income(income)
        
        elif choice == "expense":
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            date = input("Enter expense date (YYYY-MM-DD): ")
            necessity = input("Is this expense essential or non-essential?: ")
            expense = Expense(amount, category, date, necessity)
            budget_manager.add_expense(expense)

        elif choice == "exit":
            break

        else:
            print("Invalid choice. Please enter 'income', 'expense', or 'exit'.")

    budget_manager.generate_report()
    budget_manager.send_alerts()

    print("Thank you for using the Personal Budget Manager!")

if __name__ == "__main__":
    main()
