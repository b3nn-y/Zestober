def isBinary(s):
    i=0
    while s!='':
        if s[i] =='0' or s[i]=='1':
            return isBinary(s[1::])
        else:
            return False
    return True
print(isBinary('benny'))
print(isBinary('01010001'))
print(isBinary('0102001'))
print(isBinary('0101ab'))
