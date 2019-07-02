class ShoppingList(object): 
    def __init__(self, name, address): 
        self.name = name
        self.address = address
        self.grocery_items = []

    def from_dict(dict): 
        return ShoppingList(dict["name"], dict["address"])    

class GroceryItem(object): 
    def __init__(self, name, quantity, price): 
        self.name = name
        self.quantity = quantity
        self.price = price 

import json
all_dicts = []
first_question_string = "Press 1 to view all lists, press 2 to create a new list, press 3 to change a specific list, or q to quit "
menu_choice = input(first_question_string)
while menu_choice != "q": 
    if menu_choice == "1": 
        with open("list_items_grocery_persistence.json") as file_object: 
            list_dictionary = json.load(file_object) 
            for i in range(len(list_dictionary)): 
                specific_list = list_dictionary[i]
                list_as_object = ShoppingList.from_dict(specific_list)
                print((i+1), "-", list_as_object.name, "at", list_as_object.address)
            menu_choice = input(first_question_string)
    if menu_choice == "2": 
        with open("list_items_grocery_persistence.json") as file_object: 
            list_dictionary = json.load(file_object)
            all_dicts += list_dictionary  
            store_name = input("What's the name of the store? ")
            address = input("What's the address? ")
            s = ShoppingList(store_name,address)
            all_dicts.append(s.__dict__)
        with open("list_items_grocery_persistence.json", "w") as file_object:
            json.dump(all_dicts,file_object)
        menu_choice = input(first_question_string)
    if menu_choice == "3": 
        with open("list_items_grocery_persistence.json") as file_object: 
            list_dictionary = json.load(file_object) 
            all_dicts.append(list_dictionary)
            for i in range(len(list_dictionary)): 
                specific_list = list_dictionary[i]
                list_as_object = ShoppingList.from_dict(specific_list)
                print((i+1), "-", list_as_object.name, "at", list_as_object.address)
            choice = int(input("Which list would you like to view? "))
            print(all_dicts[choice])
            
