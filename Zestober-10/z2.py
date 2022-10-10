def doubleLetters(x):
    l = len(x)
    halfLen = int((l/2)-0.5)
    hl =halfLen
    j=0
    finalWord =" "
    while j<=halfLen+1:
        for i in range(0,halfLen+1):
            finalWord = finalWord+ x[j]
        j+=1
        halfLen-=1
    finalWord = finalWord+ x[hl]
    j+=1
    halfLen=2
    while j<=l-1:
        for i in range(0,halfLen):
            finalWord = finalWord+ x[j]
        j+=1
        halfLen+=1
    print(finalWord)
        
x=input("Enter a word with odd number of letters: ")
doubleLetters(x)        
