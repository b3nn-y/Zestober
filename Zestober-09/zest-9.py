def valOfName(name):
    letters = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #Creating a list of letters
    val=0
    totValue=0
    d = {}
    for i in letters: #Assigning a value for each letter inside a dict by using a for loop
        d[i] =val
        val+=1
    for i in name:
        totValue += d[i]
    print(f"The numeric value of '{name}' is {totValue}") #Finally adding them up


name = input("Enter your name: ")
valOfName(name)
