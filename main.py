import os 
tasks = []
deleted_tasks = []
completed_tasks = []
users = []
owner = "Prathamesh"
def starting():
    if os.path.exists("users"):
        with open("users","r")as file:
            for i in file:
                users.append(f"{i}\n")
user_count = len(users)
def starting_user(name):
     tasks.clear()
     completed_tasks.clear()
     deleted_tasks.clear()
     if os.path.exists(f"tasks for user {name}"):
        file_path = f"tasks for user {name}"
        with open(file_path, "r") as file:
            for i in file:
                tasks.append(f"{i}\n")

def add_task(name):
    task = input("Enter the task:- ")
    tasks.append(task)
    return f"{task} is added as task for you {name}"
def delete_task(name):
    index = int(input("Enter the number of task:-"))
    if index <= len(tasks):
        task = tasks[index-1]
        tasks.pop(index - 1 )
        deleted_tasks.append(task)
        return f"{name} your task is deleted"
    else:
        return "Nah man, go to school."
def complete(name):
    index  = int(input("enter the number of task:-"))
    if index <= len(tasks):
        task = tasks[index-1]
        tasks.pop(index - 1 )
        completed_tasks.append(task)
        return f"{name} your task is marked as complited."
    else:
        return "nah man go to school."
def view(name):
    print(f"{name} your active tasks-")
    for i in range(len(tasks)):
        print(f"\t{i+1}. {tasks[i]} ")
    if len(completed_tasks) > 0:
        print("")
        print(f"{name}your completed tasks-")
        for i in range(len(completed_tasks)):
            print(f"\t{i+1}. {completed_tasks[i]} ")
    else:
        print("")
        print("No tasks are completed yet")
    if len(completed_tasks) > 0:
        print("")
        print(f"{name} your deleted_tasks-")
        for i in range(len(deleted_tasks)):
            print(f"\t{i+1}. {deleted_tasks[i]} ")
    else:
        print("")
        print("No tasks are deleted yet")
def save(name):
    if name in users:
        for i in users:
            if i == name:
                file_path = f"tasks for user {name}"
                with open(file_path,"w") as file:
                    for task in tasks:
                        file.write(f"{task}\n")
    else:
        users.append(name)
        file_path = f"tasks for user {name}"
        with open(file_path,"w") as file:
                    for task in tasks:
                        file.write(f"{task}\n")
    print("tasks saved for you")
def load(name):
    if name in users:
        for i in users:
            if i == name:
                file_path = f"tasks for user {name}"
                with open(file_path,"r") as file:
                    for i in file:
                       print(i)
    else:
        print("First save your name by choosing '5' as your choice")

def admin():
    while(True):
        print("Things you can do\n" \
              "1. view all users\n" \
              "2. delete user\n" \
              "3. exit")
        print("")
        ch = int(input("Enter your choice:- "))
        if ch == 1:
            with open("users", "r") as file:
                for i in file:
                    print(i)
        elif ch == 2:
            file_path = users
            line_number = int(input("sr.no. of user."))
            with open(file_path, "r") as file:
                lines = file.readlines()
            if line_number < 1 or line_number > len(lines):
                print("Invalid line number")
                return
            lines.pop(line_number - 1)
            with open(file_path, "w") as file:
                file.writelines(lines)
            print("user deleted successfully")
        elif ch == 3:
            start()
        else:
            print("cant you read ? ")

def user(name):
    while(True):
        print("Things you can do\n" \
        "1. Add task\n" \
        "2. view all tasks\n" \
        "3. complete task\n" \
        "4. delete task\n"\
        "5. save task\n" \
        "6. load task\n" \
        "7. exit")
        print("")
        ch = int(input("Enter your choice:- "))
        if ch == 1:
            print("")
            print(add_task(name))
            print("\n")
        elif ch == 2:
            print("")
            print(view(name))
            print("\n")
        elif ch == 3:
            print("")
            print(complete(name))
            print("\n")
        elif ch == 4:
            print("")
            print(delete_task(name))
            print("\n")
        elif ch == 5:
            print("")
            save(name)
            print("\n")
        elif ch == 6:
            print("")
            load(name)
            print("\n")
        elif ch == 7:
            with open("users", "w") as file:
                for i in users:
                    file.write(f"{i}\n")
            save(name)
            start()
        else:
            print("cant you read ?")
def start():
    starting()
    name = input("Enter your name:- ")
    if name == owner.lower():
        admin()
    else:
        starting_user(name)
        user(name)
start()
