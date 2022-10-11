def reverse(x):
    d =0
    b=0
    countOfLength = 0
    c =x
    while c>1:
        c = c/10
        countOfLength+=1  #Finding the len of the num
    countOfLength -=1
    a = int(x/10**countOfLength)
    x = x - a * 10**countOfLength  #Getting each num one by one
    b = a  #Assigning first digit
    for i in range(countOfLength):
        d+=1
        countOfLength -=1
        a = int(x/10**countOfLength)
        x = x - a * 10**countOfLength  #Adding each num one by one
        b+= a*10**d
    return(b)

a = int(input("Enter any number: "))
print(f"The reverse of the num {a} is: ",reverse(a))




