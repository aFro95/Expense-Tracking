# Expense Tracker

This Python project provides two solutions for tracking expenses: one using JSON for data storage and another using SQLite. Both solutions allow you to add, remove, view, and summarize expenses.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Usage](#usage)
  - [JSON Solution](#json-solution)
  - [SQLite Solution](#sqlite-solution)
- [License](#license)

## Description

The Expense Tracker project is designed to help users keep track of their expenses. Users can add new expenses, remove existing ones, view a summary of their expenses, and get the total amount spent. The project includes two implementations: one using JSON for storing data and another using SQLite.

## Features

- Add new expenses with date, description, and amount.
- Remove expenses by their index or ID.
- View a list of all expenses.
- View the total amount of expenses.
- JSON solution stores expenses in a JSON file.
- SQLite solution stores expenses in an SQLite database.

## Usage

### JSON Solution

1. **Run the Program**: Execute the Python script for the JSON solution:
    ```sh
    python expense.py
    ```

2. **Follow the Prompts**: The program will prompt you to add, remove, view, or total expenses.

### SQLite Solution

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
