lst = []
def display_lst_tasks():
    print("\n To-Do-List Menu")
    print("\n 1.Display all the elments inside the lst")
    print("\n 2.Append the element to the list")
    print("\n 3.Remove the element from the lst")
    print("\n 4.Exit the program")
while True:
    display_lst_tasks()
    choice = input("\n Enter the choice (1-4):")
    if choice == "1":
        print("\n Your to-do-List:")
        if not lst:
            print("\n Nothing inside the List/empty List")
        else:
            for i,item in enumerate(lst,1):
                print(i,":",item)
    elif choice == "2":
        task = int(input("\n Enter the task: "))
        lst.append(task)
        print(f'\n"{task}", is added to your list!')
    elif choice == "3":
        print("\n your To-Do List:")
        for i,item in enumerate(lst,1):
            print("\n",i,":",item)
        try:
            task_number = int(input("\n Enter task number to remove: \n"))
            removed_number = lst.pop(task_number - 1)
            print(removed_number,"removed from the List")
        except(IndexError,ValueError):
            print("\n Invalid Task number")
    elif choice == "4":
        print("\n Exiting...Have a productive day!")
        break
    else:
        print("\n invalid choice")

