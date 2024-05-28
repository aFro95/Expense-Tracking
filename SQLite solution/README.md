# Expense Tracker (SQLite)

This Python project allows you to track your expenses using an SQLite database for data storage. You can add, remove, view, and summarize your expenses through a command-line interface.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Usage](#usage)
- [License](#license)

## Description

The Expense Tracker (SQLite) project stores expenses in an SQLite database. Users can perform various actions such as adding new expenses, removing existing ones, viewing a list of all expenses, and summarizing expenses by month and category.

## Features

- Add new expenses with date, description, category, and amount.
- Remove expenses by their ID.
- View a list of all expenses.
- View monthly expenses summarized by category.
- Data is stored in an SQLite database for persistence.

## Usage

1. **Set Up the Database**: Ensure you have SQLite installed and create a database named `expenses.db` with the necessary table.
    ```sql
    CREATE TABLE expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Date TEXT,
        description TEXT,
        category TEXT,
        price REAL
    );
    ```

2. **Run the Program**: Execute the Python script for the SQLite solution:
    ```sh
    python main.py
    ```

3. **Follow the Prompts**: The program will prompt you to add, remove, view, or summarize expenses.

## License

This project is licensed under the MIT License.
