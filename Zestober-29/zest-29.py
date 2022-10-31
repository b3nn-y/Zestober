def sameElements(lst1,lst2):
    if len(lst1) != len(lst2):
        return False
    while len(lst1)!=0:
        for i in range(len(lst2)):
            if lst1[0]== lst2[i]:
                lst1.pop(0)
                lst2.pop(i)
                return sameElements(lst1,lst2)
        return False
    return True

a=[1,1,2,1,3,2,1,4,6,2,4,5,2]
b=[2,2,1,2,2,4,2,4,6,1,4,6,2]
print(f'List1={a},List2={b},{sameElements(a,b)}')
