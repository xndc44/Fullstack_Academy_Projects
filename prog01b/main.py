import json
import os
import uuid
from prog01b.Task import Task
from prog01b.User import User


def login_and_register(users):
    while True:
        user = input('Please enter your username: ')
        password = input('Please enter your password: ')

        for u in users:
            if u['Username'] == user:
                if u['Password'] == password:
                    return u
                else:
                    print('Wrong username and password combination')
                    break
        else:
            new_user = {'Username': user, 'Password': password, 'Tasks': []}
            users.append(new_user)
            return new_user


def add_task():
    task = {
        'Task ID' : str(uuid.uuid4()),
        'Description' : input('Enter a description: '),
        'Status': 'Pending'
    }
    current_user['Tasks'].append(task)
    print('Task successfully added')

def view_tasks():
    for task in current_user['Tasks']:
        print(task)
        
def mark_as_complete():
    view_tasks()
    while True:
        task_id = input('Enter the Task ID to mark as complete: ')
        for task in current_user['Tasks']:
            if task['Task ID'] == task_id:
                task['Status'] = 'Completed'
                print('Task marked as complete')
                return
        else:
            print('Task ID not found')



def delete_task():
    view_tasks()
    while True:
        try:
            task_id = input('Enter the Task ID to delete: ')
            for task in current_user['Tasks']:
                if task['Task ID'] == task_id:
                    current_user['Tasks'].remove(task)
                    print('Task successfully deleted')
                    return
        except KeyError:
            print('The Task ID you entered is incorrect or does not exist')

def save_data(users):
    with open(file_path, 'w') as file:
        json.dump(users, file, indent=4)
        file.close()

def read_data():
    # file exists
    usernames = []
    users = []
    if not os.path.exists(file_path):
        return users

    with open(file_path, 'r') as file:
        content = file.read()
        if content == '': return []
        return json.loads(content)


if __name__ == '__main__':
    file_path = r'task_information.json'
    users = read_data()
    current_user = login_and_register(users)
    a = '''Type 1 to Add a Task
    Type 2 to View Tasks
    Type 3 to Mark a Task as Completed
    Type 4 to Delete a Task
    Type 5 to Logout\n'''
    while True:
        try:
            num = float(input(a))
            if num not in range(1, 6):
                raise ValueError()
            if num == 1: add_task()
            elif num == 2: view_tasks()
            elif num == 3: mark_as_complete()
            elif num == 4: delete_task()
            else:
                save_data(users)
                exit()

        except ValueError:
            print('Please enter a number 1-5')
