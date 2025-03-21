from flask import Flask, render_template, request, redirect, url_for
from app import app
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import os



# Path to the CSV file
EXPENSES_FILE = 'expenses.csv'

# Ensure the CSV file exists
if not os.path.exists(EXPENSES_FILE):
    with open(EXPENSES_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Amount', 'Category', 'Date'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        amount = request.form['amount']
        category = request.form['category']
        date = datetime.today().strftime('%Y-%m-%d')

        with open(EXPENSES_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([amount, category, date])

        return redirect(url_for('index'))
    return render_template('add_expense.html')

@app.route('/view')
def view_expenses():
    expenses = []
    with open(EXPENSES_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            expenses.append(row)
    return render_template('view_expenses.html', expenses=expenses)

@app.route('/summary')
def summarize_expenses():
    categories = {}
    total_amount = 0  # Initialize total amount

    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            category = row[1]
            amount = float(row[0])
            total_amount += amount  # Add to total amount

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

    return render_template('summary.html', categories=categories, total_amount=total_amount)