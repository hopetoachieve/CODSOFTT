# todo_damn.py

import json, os, random, time
from colorama import Fore, Style, init
from tqdm import tqdm

init(autoreset=True)

FILE_NAME = "tasks.json"
XP_FILE = "xp.txt"
tasks = []
xp = 0

# Fun Quotes & Responses
quotes = [
    "Keep going, you magnificent beast! ",
    "You just deleted a task like a pro ninja ",
    "That task never saw it coming... BOOM ",
    "Another one bites the dust ",
    "Get things done, or they get YOU ",
    "Let’s wreck that task list like a boss "
]

responses = [
    "Fine, I added your task. Happy now?",
    "You better finish this one!",
    "Added to your chaos pile... I mean task list.",
    "Task added. You owe me one 👀"
]

# ----------------------------------
# FILE HANDLING
# ----------------------------------
def load_tasks():
    global tasks
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            tasks = json.load(f)

def save_tasks():
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def load_xp():
    global xp
    if os.path.exists(XP_FILE):
        with open(XP_FILE, "r") as f:
            xp = int(f.read())

def save_xp():
    with open(XP_FILE, "w") as f:
        f.write(str(xp))

# ----------------------------------
# APP FUNCTIONS
# ----------------------------------
def show_banner():
    print(Fore.CYAN + Style.BRIGHT + "\n BEST TO-DO LIST EVER🌟")
    print(random.choice(quotes))

def show_menu():
    print(Fore.YELLOW + "\n--- What shall we do today, hmm? ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Secret Command")
    print("6. Exit")

def add_task():
    task = input("✍️  What’s the task ? > ")
    tasks.append({"task": task, "done": False})
    print(Fore.GREEN + random.choice(responses))

def view_tasks():
    print("\n Your Glorious Task List:")
    if not tasks:
        print(" Nothing here but dreams. Add something!")
        return
    for idx, t in enumerate(tasks):
        status = Fore.GREEN + "✅" if t["done"] else Fore.RED + "❌"
        print(f"{Fore.MAGENTA}{idx+1}. {t['task']} [{status}]")

def mark_done():
    view_tasks()
    try:
        index = int(input(" Task number to complete? > ")) - 1
        if 0 <= index < len(tasks):
            if not tasks[index]["done"]:
                tasks[index]["done"] = True
                global xp
                xp += 10
                print(Fore.CYAN + f" Task crushed! You gained 10 XP. Total XP: {xp}")
            else:
                print(" Already done, show-off.")
        else:
            print(" Invalid number.")
    except:
        print(" That's not a number!")

def delete_task():
    view_tasks()
    try:
        index = int(input("🗑️  Task to vaporize? > ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print(Fore.RED + " Boom! Task obliterated into the void.")
            print(random.choice(quotes))
        else:
            print("⚠️ Invalid number.")
    except:
        print(" That's not a number!")

def secret_command():
    print(Fore.YELLOW + "\n👀 You found the secret chamber...")
    print("Here's your fortune cookie:")
    print(Fore.MAGENTA + random.choice(quotes))
    print(Fore.GREEN + "You’ve earned 5 bonus XP 🎁 just for being curious.")
    global xp
    xp += 5

# ----------------------------------
# APP LAUNCH
# ----------------------------------
load_tasks()
load_xp()
show_banner()

# Mood Select
mood = input("\n What’s your vibe today? (😎/😡/🤖): ")
if mood == "😎":
    print("😎 Chill mode activated. Slay peacefully.")
elif mood == "🤖":
    print("🤖 System operational. Executing mission.")
elif mood == "😡":
    print("😡 Let's smash tasks with rage!")

# Loop
while True:
    show_menu()
    choice = input(" Enter your choice (1-6): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5" or choice.lower() == "secret" or choice == "42":
        secret_command()
    elif choice == "6":
        print(Fore.CYAN + "Saving your progress...")
        for i in tqdm(range(10), desc="💾 Saving..."):
            time.sleep(0.05)
        save_tasks()
        save_xp()
        print(Fore.GREEN + " Bye bye, legend! Stay productive.")
        break
    else:
        print(Fore.RED + " That’s not even a valid option. Try again.")
