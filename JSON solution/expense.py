import json

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()  # Load existing expenses from file

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.save_expenses()  # Save updated expenses to file

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            self.save_expenses()  # Save updated expenses to file
            print("Expense removed successfully!")
        else:
            print("Invalid expense index")

    def view_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses found!")
        else:
            print("Expense List:")
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}. Date: {expense['date']}, Description: {expense['description']}, Amount: {expense['amount']} Lei")

    def total_expenses(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"Total expenses: {total:.2f} Lei")

    def load_expenses(self):
        try:
            with open("expenses.json", "r") as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            # File doesn't exist, initialize with an empty list
            self.expenses = []

    def save_expenses(self):
        with open("expenses.json", "w") as file:
            json.dump(self.expenses, file)

    @staticmethod
    def main():
        tracker = ExpenseTracker()
        print(f"🤑 Running Expense Tracker!")

        while True:
            print("\nWhat would you like to do?")
            print("1. Add Expense")
            print("2. Remove Expense")
            print("3. View Expenses")
            print("4. Total Expenses")
            print("5. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                date = input("Enter the date (YYYY-MM-DD): ")
                description = input("Enter the description: ")
                amount = float(input("Enter the amount (Lei): "))
                expense = {"date": date, "description": description, "amount": amount}
                tracker.add_expense(expense)
                print("Expense added successfully!")
            elif choice == "2":
                index = int(input("Enter the index of the expense to remove: ")) - 1
                tracker.remove_expense(index)
            elif choice == "3":
                tracker.view_expenses()
            elif choice == "4":
                tracker.total_expenses()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    ExpenseTracker.main()
