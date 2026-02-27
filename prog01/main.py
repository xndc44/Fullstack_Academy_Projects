import datetime
import re
import os
import json

def get_date():
    date_of_expense = input('Enter the date of the expense in the format YYYY-MM-DD ')
    pattern = r'\d{4}-\d{2}-\d{2}'
    d = ''
    while True:
        try:
            match = re.fullmatch(pattern, date_of_expense)
            if not match:
                date_of_expense = input('Please use the format YYYY-MM-DD ')
            else:
                s = list(map(int, date_of_expense.split('-')))
                d = datetime.date(s[0], s[1], s[2])
                break
        except ValueError:
            print('Please enter a valid date')
            date_of_expense = input('Please use the format YYYY-MM-DD ')
    return d.strftime('%Y-%m-%d')


def get_category():
    category = input('Enter the category of the expense (Food or Travel) ')
    while category not in ['Food', 'Travel']:
        category = input('Please enter either \'Food\' or \'Travel\' ')
    return category

def get_amount():
    amount = 0
    while True:
        try:
            amount = float(input('Enter your amount spent '))
            if amount < 0:
                raise ValueError('Value cannot be negative') 
            break
        except ValueError:
            print('Please enter a valid number ')
    return str(amount)

def get_description():
    return input('Please enter a brief description of the expense ')

def add_expense():
    expense = {}
    expense['date'] = get_date()
    expense['category'] = get_category()
    expense['amount'] = get_amount()
    expense['description'] = get_description()
    expenses.append(expense)

def view_expenses():
    for exp in expenses:
        for k in exp:
            if not exp[k]:
                if k == 'date':
                    exp['date'] = get_date()
                elif k == 'category':
                    exp['category'] = get_category()
                elif k == 'amount':
                    exp['amount'] = get_amount()
                else:
                    exp['description'] = get_description()
        print(exp)

def track_budget():
    while True:
        try:
            budget = float(input('Enter your budget'))
            if budget < 0:
                raise ValueError('Value cannot be negative') 
            spent = sum(float(exp['amount']) for exp in expenses)
            if spent > budget:
                print('You have exceeded your budget!')
            else:
                print(f'You have {budget - spent} left for the month')
            break
        except ValueError:
            print('Please enter a valid number ')
    

def save_expenses():
    with open(file_path, 'w') as file:
        json.dump(expenses, file, indent=4)
        file.close()

def read_expenses():
    # file exists
    global file_path
    global expenses
    file_path = r'prog01\\expenses.json'
    if not os.path.exists(file_path):
        expenses = []
        return
    
    with open(file_path, 'r') as file:
        expenses = json.load(file)

if __name__ == '__main__':
    a = '''Type 1 to Add expense
    Type 2 to View expenses
    Type 3 to Track budget
    Type 4 to Save expenses
    Type 5 to Exit\n'''
    read_expenses()
    while True:
        try:
            num = float(input(a))
            if num not in range(1, 6):
                raise ValueError()
            if num == 1: add_expense()
            elif num == 2: view_expenses()
            elif num == 3: track_budget()
            elif num == 4: save_expenses()
            else:
                save_expenses()
                exit()
        except ValueError:
            print('Please enter a number 1-5')