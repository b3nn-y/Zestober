def sumOfInt(x):
    b= a.split(';')
    s=0
    for i in  b:
        s+=int(i)
    print(s)


a= input("Enter few numbers seperated by';': ")
sumOfInt(a)
