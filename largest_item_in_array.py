numbers = [3,4,5,6,7,8,9,10, -9, 15]
def find_largest_number(array): 
    current_largest_number = array[0]
    for item in array: 
        if item > current_largest_number: 
            current_largest_number = item
    return current_largest_number
 
print(find_largest_number(numbers))

