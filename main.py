import csv
from datetime import datetime
import matplotlib.pyplot as plt

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = datetime.today().strftime('%Y-%m-%d')
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, date])
    print("Expense added successfully!")

def view_expenses():
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def summarize_expenses():
    categories = {}
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            category = row[1]
            amount = float(row[0])
            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

    # Plotting
    plt.bar(categories.keys(), categories.values())
    plt.xlabel('Categories')
    plt.ylabel('Total Spending')
    plt.title('Spending by Category')
    plt.show()            

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")
    
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summarize_expenses()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

