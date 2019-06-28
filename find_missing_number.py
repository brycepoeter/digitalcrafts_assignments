numbers_missing = [0,1,2,3,4,5,7,8,9]
def find_missing_number(array): 
    numbers = [0,1,2,3,4,5,6,7,8,9]
    for item in numbers: 
        if item not in array: 
            print(f"The missing number is {item}")
 
find_missing_number(numbers_missing)