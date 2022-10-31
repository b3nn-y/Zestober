def oneAway(s,t,count):
    if len(s)!=len(t):
        return False
    while s!='':
        if s[0]!=t[0]:
            count+=1
            return oneAway(s[1:],t[1:],count)
        else:
            return oneAway(s[1:],t[1:],count)
    if count ==1:
        return True
    else:
        return False
a,b='benny','penny'
print(f'Word 1={a},Word 1={b}',oneAway(a,b,0))
