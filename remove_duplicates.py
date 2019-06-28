names = ["Alex","John","Mary","Steve","John", "Steve"]
def remove_duplicates(array): 
    names_new = []
    for item in names: 
        if item not in names_new: 
            names_new.append(item)
    return names_new
 
print(remove_duplicates(names))