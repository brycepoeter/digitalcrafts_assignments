import json 
all_tasks = []
opening_menu = input("Hello! Please select a command. Press 1 to add a task, 2 to delete a task, 3 to view all tasks, or q to quit ")
while opening_menu != "q": 
    if opening_menu == "1": 
        name = input("What's the name of the task? ")
        priority = input("Is this High, Medium, or Low priority? ")
        new_dict = {"Name": name, "Priority": priority}
        all_tasks.append(new_dict)
        with open("todo_list_items.json", "w") as file_object: 
            json.dump(all_tasks, file_object)
        opening_menu = input("Hello! Please select a command. Press 1 to add a task, 2 to delete a task, 3 to view all tasks, or q to quit ")
    if opening_menu == "2": 
        for i in range(len(all_tasks)): 
            print((i + 1), "-", all_tasks[i]["Name"], "(", all_tasks[i]["Priority"], "Priority", ")") 
        delete_choice = int(input("Which task would you like to delete? "))
        all_tasks.pop(delete_choice - 1)
        with open("todo_list_items.json", "w") as file_object: 
            json.dump(all_tasks, file_object)
        opening_menu = input("Hello! Please select a command. Press 1 to add a task, 2 to delete a task, 3 to view all tasks, or q to quit ")
    if opening_menu == "3": 
        for i in range(len(all_tasks)): 
            print((i + 1), "-", all_tasks[i]["Name"], "(", all_tasks[i]["Priority"], "Priority", ")")
        opening_menu = input("Hello! Please select a command. Press 1 to add a task, 2 to delete a task, 3 to view all tasks, or q to quit ")

