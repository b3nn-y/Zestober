def hasConsecutiveRepeat(s,i):
    return s[i]

def repeat(s):
    i = 0
    while s!='' and i<len(s)-1:
        if s[i]== hasConsecutiveRepeat(s,i+1):
            return True
        else:
            i+=1
    return False
print(repeat('benny'))
