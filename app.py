import sqlite3
from datetime import datetime
from tzlocal import get_localzone
import tabulate
import os
import keyboard

local_tz = get_localzone()
current_time = datetime.now(local_tz)
formatted_time = current_time.strftime("%Y-%m-%d    %H:%M:%S")

db = sqlite3.connect('tasks.db')
cur = db.cursor()



cur.execute(""" CREATE TABLE IF NOT EXIST tasks(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            date TEXT NOT NULL,
            status TEXT NOT NULL,    
            )
""")



def clear():
    os.system('cls')



def add_task():
    clear()
    task = input("Enter The Task : ")
    date = str(formatted_time)
    status = 'Not Started'
    cur.execute("INSERT INTO tasks (task, date, status) VALUES (?, ?, ?)", (task, date, status))
    print("Task Added Successfuly !")
    db.commit()

def view_tasks():
    clear()
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    headers = ["ID", "Task", "Date", "Status"]
    print(tabulate.tabulate(tasks, headers, tablefmt='orgtbl'))

def delete_task():
    view_tasks()
    while True:
        try:
            task_id = int(input("Enter The id of the task you want to delete: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    cur.execute("DELETE FROM tasks WHERE ID =?",(task_id,))
    db.commit()


def update_task():
    while True:
        try:
            task_id = input("Enter The Task Id To Update : ")
            break
        except ValueError:
            print("Invalid Input. Enter A Valid Integer Number")
    new_task = input("Enter The New Task")
    cur.execute("UPDATE tasks SET task=? WHERE id=?",(new_task,task_id))
    print("Task Updated Successfuly")
    db.commit()


def markStarted():
    while True:
        try:
            task_id = int(input("Enter The Task Id To Mark It As Started :"))
            break
        except ValueError:
            print("Invalid Input, Enter A Valid Number.")
    cur.execute("UPDATE tasks SET status=? WHERE id=?",('Started',task_id))
    db.commit()


def markFinished():
    while True:
        try:
            task_id = int(input("Enter The Task Id To Mark It As Finished :"))
            break
        except ValueError:
            print("Invalid Input. Enter A Valid Number")
    cur.execute("UPDATE tasks SET status=? WHERE id=?",('Finished',task_id))
    print("Task Marked As Finished Successfuly")
    db.commit()


if __name__ == "__main__":
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Update Task")
        print("5. Mark Task As Started")
        print("6. Mark Task As Finished")
        print("7. Exit")
        choice = input("Enter Your Choice : ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            update_task()
        elif choice == '5':
            markStarted()
        elif choice == '6':
            markFinished()
        elif choice == '7':
            break
        else:
            print("Invalid Choice. Please Enter A Valid Choice")
        print("Press Enter To Continue...")
        keyboard.wait('enter')
        clear()