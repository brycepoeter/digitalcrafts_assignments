import datetime
import json


def get_current_time(): 
    current_time = datetime.datetime.now()
    return current_time.strftime("%H:%M:%S")

def reserve_a_table(): 
    display_status_all_tables()
    table_number = int(input("Which table would you like to reserve? "))  
    if check_if_available(table_number) == False: 
        print("I'm sorry, that table is reserved ")
    if check_if_available(table_number) == True: 
        all_tables[table_number - 1]["Start time"] = get_current_time()

def end_playing_session(): 
    get_occupied_tables()
    choice = int(input("Which session would you like to end? "))
    all_tables[choice - 1]["End time"] = get_current_time()
    new_dict = {"Table": all_tables[choice - 1]["Table"], "Start time": all_tables[choice - 1]["Start time"], "End time": all_tables[choice - 1]["End time"], "Total time": [], "Cost": []}
    calculate_total_time(new_dict)
    new_dict["Total time"] = calculate_total_time(new_dict)
    print(f"Your total usage was {calculate_total_time(new_dict)}") 
    cost = calculate_cost(new_dict) 
    new_dict["Cost"] = cost
    print("Your total cost was ", cost)
    all_receipts.append(new_dict)

def reset_table(): 
    for i in range(len(all_tables)):   
        if all_tables[i]["End time"] != "-": 
            all_tables[i]["End time"] = "-"
            all_tables[i]["Start time"] = "-"

def check_if_available(table): 
    available = False 
    if all_tables[table - 1]["Start time"] == "-": 
        available = True 
    return available 

def display_table_status(table): 
    result = check_if_available(table)
    if result == True: 
        print("Table", all_tables[table - 1]["Table"], "is AVAILABLE")
    if result == False: 
        print("Table", all_tables[table - 1]["Table"], "is IN USE") 

def display_status_all_tables(): 
    for i in range(len(all_tables)): 
        display_table_status(i + 1)

def get_occupied_tables(): 
    for i in range(len(all_tables)):
        status = check_if_available(i)
        if status == False: 
            print("Table", all_tables[i - 1]["Table"], "is IN USE") 
      

def calculate_total_time(dict): 
    end_time = dict["End time"].split(":")
    start_time = dict["Start time"].split(":") 
    hour_difference = int(end_time[0]) - int(start_time[0])
    minute_difference = int(end_time[1]) - int(start_time[1])
    second_difference = int(end_time[2]) - int(start_time[2])
    if second_difference < 0: 
        second_difference = 60 + second_difference  
        minute_difference -= 1
    total_time = f"{hour_difference} hours, {minute_difference} minutes, {second_difference} seconds"
    return total_time

def calculate_cost(dict): 
    cost = 0
    end_time = dict["End time"].split(":")
    start_time = dict["Start time"].split(":") 
    hour_difference = int(end_time[0]) - int(start_time[0])
    minute_difference = int(end_time[1]) - int(start_time[1])
    second_difference = int(end_time[2]) - int(start_time[2])
    if second_difference < 0: 
        second_difference = 60 + second_difference  
        minute_difference -= 1
    cost = (hour_difference * 30) + (minute_difference * 30 / 60) + (second_difference * 30 / 60 / 60)
    return cost 

def backup_to_json(): 
    todays_date = datetime.datetime.now().strftime("%b_%d_%Y") 
    with open(f"{todays_date}.json", "w") as file_object: 
        json.dump(all_receipts, file_object) 


all_tables = []
all_receipts = []
main_menu_prompt = "What would you like to do? Press 1 to view all tables, Press 2 to reserve a table, Press 3 to end a session, or Press q to end the session "

for i in range(1,13): 
    table = {"Table": i, "Start time": "-", "End time": "-", "Total time": "-", "Cost": "-"}
    all_tables.append(table)
main_menu = input(main_menu_prompt)
while main_menu != "q": 
    if main_menu == "1": 
        display_status_all_tables()
        main_menu = input(main_menu_prompt)
    if main_menu == "2":
        reserve_a_table()
        main_menu = input(main_menu_prompt)
    if main_menu == "3": 
        end_playing_session()
        reset_table()
        backup_to_json()
        main_menu = input(main_menu_prompt)

backup_to_json()

print("~~~~~ Your total receipts for the day were ~~~~~ \n", all_receipts)


