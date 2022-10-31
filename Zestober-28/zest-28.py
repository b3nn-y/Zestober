def containsNegativePair(List,i):
    l= len(List)
    while i<l-1:
        if List[i] + List[i+1] ==0:
            return True
        else:
            return containsNegativePair(List,i+1)
    return False

a=[1,2,3,4]
print(f'List={a},{containsNegativePair(a,0)}')
