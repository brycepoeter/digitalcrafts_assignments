current_tasks = []
user_decision_123 = input("Press 1 to add a task, 2 to delete a task, 3 to view all tasks, or q to quit ")
while user_decision_123 != "q":   
        if user_decision_123 not in ["1","2","3"]:
            print("I don't understand.") 
            user_decision_123 = input("Press 1 to add a task, 2 to delete a task, 3 to view all tasks, or q to quit ")
        if user_decision_123 == "1": 
            new_dict = {}
            title = input("What task would you like to add? ")
            priority = input("Is this task high, medium, or low priority? ")
            new_dict["Task"] = title 
            new_dict["Priority"] = priority
            current_tasks.append(new_dict)
            user_decision_123 = input("Press 1 to add a task, 2 to delete a task, 3 to view all tasks, or q to quit ")
        if user_decision_123 == "2":
            for i in range(len(current_tasks)): 
                print(i + 1, current_tasks[i]["Task"], "-", current_tasks[i]["Priority"])
            desired_item = int(input("Which item number would you like to delete? "))
            del current_tasks[desired_item - 1]
            user_decision_123 = input("Press 1 to add a task, 2 to delete a task, 3 to view all tasks, or q to quit ")
        if user_decision_123 == "3": 
            for i in range(len(current_tasks)): 
                print(i + 1, current_tasks[i]["Task"], "-", current_tasks[i]["Priority"])
            user_decision_123 = input("Press 1 to add a task, 2 to delete a task, 3 to view all tasks, or q to quit ")
    

                