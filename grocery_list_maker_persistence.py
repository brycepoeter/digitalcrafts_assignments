class ShoppingList(object): 
    def __init__(self, name, address): 
        self.name = name
        self.address = address
        self.grocery_items = []
    def from_dictionary(dictnry): 
        return ShoppingList(dictnry["name"], dictnry["address"])

class GroceryItem(object): 
    def __init__(self, name, quantity, price): 
        self.name = name
        self.quantity = quantity
        self.price = price 

import json
first_question_string = "Press 1 to create a new list, press 2 to display all existing lists, press 3 to change a specific list, or q to quit "

set_of_all_lists = []
first_question = input(first_question_string) 
while first_question != "q": 
    if first_question == "1": 
        store_name = input("What's the name of the store? ")
        address = input("What's the store's address? ") 
        s = ShoppingList(store_name, address)
        s_dict = s.__dict__
        set_of_all_lists.append(s_dict)
        with open("list_items_grocery_persistence.json", "w") as file_object: 
            json.dump(set_of_all_lists, file_object)
        first_question = input(first_question_string) 
    if first_question == "2": 
        with open("list_items_grocery_persistence.json") as file_object: 
            json.load(file_object)
            ShoppingList.from_dictionary(file_object)
        #for i in range(len(set_of_all_lists)): 
            #current_list_working = set_of_all_lists[i]
            #print(f"~~~~~~Shopping List for {current_list_working.name}~~~~~~") 
            #for item in current_list_working.grocery_items: 
                #print(f"{item.name} Cost: ${item.price} Need: {item.quantity}")
        first_question = input(first_question_string) 
    if first_question == "3":  
        for i in range(len(set_of_all_lists)): 
            print((i+1), "-", set_of_all_lists[i]["name"], "at", set_of_all_lists[i]["address"])
        answer = int(input("Which list would you like to change? "))
        shopping_list_working = set_of_all_lists[answer - 1]
        add_or_view = int(input("What would you like to do? Press 1 to add an item to the list or press 2 to view current items "))
        if add_or_view == 1: 
            name = input("What's the item's name? ")
            quantity = int(input("How many do you need? "))
            price = int(input("How much does each one cost? "))
            grocery_item = GroceryItem(name, quantity, price)
            grocery_item_dict = grocery_item.__dict__
            shopping_list_working.grocery_items.append(grocery_item)
            with open("list_items_grocery_persistence.json", "w") as file_object: 
                json.dump(set_of_all_lists, file_object)
            first_question = input(first_question_string) 
        if add_or_view == 2: 
            print(f"~~~~~~Shopping List for {shopping_list_working.name}~~~~~~")
            for item in shopping_list_working.grocery_items: 
                print(f"{item.name} Price: ${item.price} Quantity needed: {item.quantity}") 
            first_question = input(first_question_string)