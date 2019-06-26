def test_prime(): 
    number = int(input("Enter a positive number: "))
    if number == 0: 
        print("Number is not prime") 
    elif number == 1: 
        print("Number is not prime")
    elif number > 1:
        for x in range(2, number): 
            if number % x == 0:
                print("Number is not prime")
                break
        else: 
            print("Number is prime")

test_prime()

