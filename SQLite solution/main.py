import sqlite3

conn = sqlite3.connect("expenses.db")
cur = conn.cursor()

while True:
    print("Select an option:")
    print("1. Add an expense")
    print("2. Remove an expense")
    print("3. View expenses summary")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        date = input("Enter the date of the expense (YYYY-MM-DD): ")
        description = input("Enter the description of the expense: ")

        cur.execute("SELECT DISTINCT category FROM expenses")

        categories = cur.fetchall()

        print("Select a category by number:")
        for idx, category in enumerate(categories):
            print(f"{idx + 1}. {category[0]}")
        print(f"{len(categories) + 1}. Create a new category")

        category_choice = int(input())
        if category_choice == len(categories) + 1:
            category = input("Enter the new category name: ")
        else:
            category = categories[category_choice - 1][0]

        price = float(input("Enter the price of the expense: "))

        cur.execute("INSERT INTO expenses (Date, description, category, price) VALUES (?,?,?,?)", (date, description, category, price))
        conn.commit()
    
    elif choice == 2:
        expense_id = int(input("Enter the ID of the expense you want to delete: "))
        cur.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        conn.commit()
        print("Expense deleted successfully.")


    elif choice == 3:
        print("Select an option: ")
        print("1. View all expenses")
        print("2. View monthly expenses by category")

        view_choice = int(input())
        if view_choice == 1:
            cur.execute("SELECT * FROM expenses")
            expenses = cur.fetchall()
            for expense in expenses:
                print(expense)
        elif view_choice == 2:
            month = int(input("Enter the month number (MM): "))
            year = int(input("Enter the year (YYYY): "))
            cur.execute("""SELECT category, SUM(price) FROM expenses 
                        WHERE strftime('%m', Date) = ? AND strftime('%Y', Date) = ? 
                        GROUP BY category""", (str(month).zfill(2), str(year)))

            expenses = cur.fetchall()
            for expense in expenses:
                print(f"Category: {expense[0]}, Total: {expense[1]} Lei")
        else:
            exit()
    elif choice == 4:
        break
    else:
        print("Invalid choice! Please enter a valid option.")


    repeat = input("Would you like to do something else? (y/n): ")
    if repeat.lower() != "y":
        break

conn.close()
