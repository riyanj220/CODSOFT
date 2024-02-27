import re

print("***Welcome to To-do list***")
to_do_list = {}
while True:
    print()
    print("What do you want ?")
    print("Option 1 : Create a to-do list \n"
          "Option 2 : Update your to-do list \n"
          "Option 3 : Track your to-do list \n" 
          "Option 4 : Exit to-do list")

    user_input = eval(input("Choose from above options: "))
    print()

    match user_input:
        case 1:
            print("Creating your to-do list.. press 'q' to exit. ")
            name = input("Enter your list name: ").strip().lower()

            with open ('to_do_list.txt','w') as f:
                f.write(f"Name: {name}\n")
                f.write("Time\t\t\tTask\n")

                while True: 
                    time=input("Enter the time: ")
                    if time.lower() == 'q':
                        break

                    task=input("Enter the task: ").lower()
                    if task.lower() == 'q':
                        break
                    print()

                    to_do_list[task] = time
                    f.write(f"{time}\t\t\t\t{task}\n")

            print("To-do list created successfully.")

        case 2:
            name = input("Enter your list name: ").strip().lower()
            with open ('to_do_list.txt') as f:
                content = f.readline().strip()
                user_name = content.split(': ')[1].lower().strip()

                if name != user_name:
                    print(f"Sorry , No to-do list found with {name} name")
                else:
                    f.seek(0)
                    next(f)
                    next(f)

                    lines = f.readlines()
                    to_do_list = {}

                    for line in lines:
                        parts = re.split(r'\s{2,}', line.strip())
                        if len(parts) >=2:
                            time = parts[0]
                            task = parts[1].strip()
                            to_do_list[task] = time

                    print("Option 1 : Remove a task\n"
                          "Option 2 : Update a task ")
                    user = eval(input("Choose from above options: "))

                    if user == 1:
                        print("Here's your to-do list \n")
                        print("Time\t\t\tTask")
                        for task, time in to_do_list.items():
                            print(f"{time}\t\t\t{task}")

                        user_remove= input("Enter task name to remove: ").strip()
                        if user_remove in to_do_list:
                            del to_do_list[user_remove]
                            print(f"Task '{user_remove}' removed successfully.")

                            with open ('to_do_list.txt','w') as f:
                                f.write(f"Name: {name}\n")
                                f.write("Time\t\t\tTask\n")
                                for time,task in to_do_list.items():
                                    f.write(f"{task}\t\t\t\t{time}\n")

                        else:
                            print(f"Task '{user_remove}' not found in the to-do list.")
                        
                    elif user == 2:
                        print("Here's your to-do list \n")
                        print("Time\t\t\tTask")
                        for task, time in to_do_list.items():
                            print(f"{time}\t\t\t{task}")

                        user_update= input("Enter task name to update: ").strip()
                        
                        if user_update in to_do_list:
                            time=input("Enter the new time: ")
                            task=input("Enter the new task name: ")
                            to_do_list[task] = to_do_list.pop(user_update)
                            to_do_list[task] = time 
                            print(f"To-do list Updated successfully.")

                            with open ('to_do_list.txt','w') as f:
                                f.write(f"Name: {name}\n")
                                f.write("Time\t\t\tTask\n")
                                for t,tsk in to_do_list.items():
                                    if len(t) == 1:
                                        indentation = "\t\t\t\t"
                                    elif len(t) ==2:
                                        indentation = "\t\t\t "
                                    elif len(t) ==3:
                                        indentation = "\t\t  "
                                    elif len(t) == 4:
                                        indentation = "\t\t   "
                                    else:
                                        indentation = "\t\t    "
                                    f.write(f"{tsk}{indentation}{t}\n")
                    
                        else:
                            print(f"Task '{user_update}' not found in the to-do list.")

        case 3:
            name = input("Enter your list name: ").strip().lower()
            with open('to_do_list.txt') as f:
                content = f.readline().strip()
                match = re.search(r'Name:\s*(.*)', content)
                user_name = match.group(1).strip().lower()  

                if name != user_name:
                    print(f"Sorry, no to-do list found with the name '{name}'.")
                else:
                    print("Here's your to-do list:")
                    print("Time\t\t\tTask")
                    f.seek(0)
                    next(f) 
                    for line in f:
                        if line.strip() != "":
                            parts = line.strip().split('\t\t\t\t')
                            if len(parts) >= 2:
                                time = parts[0]
                                task = parts[1]
                                print(f"{time}\t\t\t{task}")

        case 4:
            print("Exiting your to-do list...")
            break

        case _:
            print("Please enter a valid option (1,2,3 or 4) ")
            continue

    
