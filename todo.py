#file opening
FILENAME="file.txt"
def load_tasks():
    try:
        with open(FILENAME,'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

    
#save tasks
def save_tasks(tasks):
    with open(FILENAME,'w') as file:
        for task in tasks:
            file.write(task+'\n')

            
#file view
def view_tasks(tasks):
    if not tasks:
        print("No tasks")
    else:
        for i,task in enumerate(tasks,1):
            print(f"{i}. {task}")

            
#file add
def add_tasks(tasks):
    task=input("enter your tasks").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("task added succesfully")
    else:
        print("task not added")

        
#file remove
def remove_tasks(tasks):
    try:
        view_tasks(tasks)
        num=int(input("Enter task no. to remove:"))
        if 1 <= num <=len(tasks):
            removed=tasks.pop(num-1)
            save_tasks(tasks)
            print(f"remove: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number")

        
def main():
    tasks=load_tasks()
    while True:
        print("\n-----------------\n")
        print("1.view tasks")
        print("2.add tasks")
        print("3.remove tasks")
        print("4.exit")

        ch=input("enter chioce")
        if ch=="1":
            view_tasks(tasks)
        elif ch=='2':
            add_tasks(tasks)
        elif ch=='3':
            remove_tasks(tasks)
        elif ch=='4':
            print("Thank You")
            break
        else:
            print("Invalid choice")

if __name__=="__main__":
    main()
