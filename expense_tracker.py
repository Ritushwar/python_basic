def add_expense(expenses,category,amount):
    expenses.append({'category':category,'amount':amount})

def print_expenses(expenses):
    for expense in expenses:
        print(f"Category: {expense['category']}, Amount: {expense['amount']}")

def total_expenses(expenses):
    total = sum(map(lambda expense: expense['amount'],expenses))
    print(f"Total expenses: {total}")

def filter_expenses(expenses,category):
    return filter(lambda expense: expense['category'] == category, expenses )

def main():
    expenses = []
    while True:
        print("1.Add Expenses")
        print("2.List all Expenses")
        print("3.Show Total Expense")
        print("4.Filter Expenses by category")
        print("5.Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            category = input("Category: ")
            amount = float(input("Amount: "))
            add_expense(expenses,category,amount)
        elif choice == '2':
            print_expenses(expenses)
        elif choice == '3':
            total_expenses(expenses)
        elif choice == '4':
            category = input("Category: ")
            expense_from_filter = filter_expenses(expenses,category)
            print_expenses(expense_from_filter)
        elif choice == '5':
            print(f"Exiting")
            break
main()