def firstDiff(s,t,i,c):
    count =c
    while i<len(t):
        if s[i]==t[i]:
            count+=1
            firstDiff(s,t,i+1,count)
        else:
            return count
    return count

print(firstDiff('abccsd','abc',0,0))
