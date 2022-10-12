def palindrome(x):
    print(x[::-1]) #Reverses the word
    if x==x[::-1]:
        print('It is a palindrome')
    else:
        print('No,It is not a palindrome')
        
word = input("Enter a word: ")
palindrome(word)
