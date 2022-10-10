def multiLetters(x):
    l =len(x)      #initializing some variables which are required
    mid = int((l/2)-0.5)
    finalstr=""
    r = mid+1
    index = 0    
    while index<=l:   #Creating the first half of the string
        for i in range(r):
            finalstr+= x[index]
        r-=1                   
        index+=1
    r2 = mid+1
    a=2
    while r2<=l-1:
        for i in range(a):
            finalstr+= x[r2]    #Second Half
        a+=1
        r2+=1
    print(finalstr)

word = input("Enter a word with odd number of letters: ")
multiLetters(word)
