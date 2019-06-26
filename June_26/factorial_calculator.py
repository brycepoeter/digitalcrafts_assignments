number = int(input("Enter a number: ")) 
def calculate_factorial(): 
    product = 1 
    if number < 0: 
        print("Factorials are undefined for negative numbers.")
    else: 
        for x in range(1, number + 1): 
            product = product * x 
        return product 

print(calculate_factorial())
    
    