def test_palindrome(): 
    word = input("Enter a word to be tested: ") 
    for x in range(0, len(word) // 2):
        if word[x] != word[len(word) - 1 - x]: 
            print("Your word is not a palindrome.")
            break
    else: 
        print("Your word is a palindrome.")

test_palindrome()
