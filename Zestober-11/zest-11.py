def multiLetters(x):
    l =len(x)      #initializing some variables which are required
    finalstr=""
    index = 0
    r=1
    while r<=l:
        for i in range(r):
            finalstr+=x[index]
            index+=1
        index=0   #adding the strings
        r+=1
        finalstr+=" "
    print(finalstr)

        
word=input("Enter a word: ")
multiLetters(word)
        

