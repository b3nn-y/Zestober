import string,random
def assortedTable(n):
    print(f'Size={n}')
    a=string.ascii_lowercase
    b=string.ascii_uppercase
    c=string.digits
    d=string.punctuation
    allCharacters=a+b+c+d
    temp=[]
    f=0
    i=0
    if n%2!=0:
        f=int((n*n)/2)+1
    else:
        f=int((n*n)/2)
    for i in range(f):
        temp.append(random.choice(allCharacters))
    temp += temp
    for i in range(n):
        for j in range(n):
            g=len(temp)-1
            index=random.randint(0,g)
            print(temp[index],end="  ")
            temp.pop(index)
        print(end="\n")
assortedTable(3)
