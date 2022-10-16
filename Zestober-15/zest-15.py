def rangoli(n): 
    l = "abcdefghijklmnopqrstuvwxyz"
    data = [l[i] for i in range(n)]
    i = list(range(n))  
    i = i[:-1]+i[::-1]
    for i in i:
        temp = data[-(i+1):]
        row = temp[::-1]+temp[1:]
        print("-".join(row).center(n*4-3, "-"))
rangoli(3)
#Got this code from the internet and understood how it works...
