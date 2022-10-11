def secLargest(a,b,c):
    if (a>b and a>c and c<a and c<b):
        return(b)
    elif (a>b and a>c and b<a and b<c):
        return(c)
    elif(b>a and b>c and a<b and a<c):
        return(c)
    elif(b>a and b>c and c<a and c<b):
        return(a)
    elif(c>a and c>b and b<a and b<c):
        return(a)
    elif (c>b and c>a and a<b and a<c):
        return(b)
a = int(input('Enter a number: '))
b=int(input('Enter a number: '))
c=int(input('Enter a number: '))

print(f"The second largest num in {a},{b},{c} is {secLargest(a,b,c)}")
