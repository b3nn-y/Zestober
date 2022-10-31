def digiRoot(n):
    if n/10<1:
        return n
    else:
        tempNum=str(n)
        c=0
        for i in tempNum:
            c+=int(i)
        return digiRoot(c) #Reccursion
x=int(input('Enter a number: '))
print(f'The Digital Root of {x} is {digiRoot(x)}')
