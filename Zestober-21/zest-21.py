def con(s,ch,i):
        if s[i]==ch:
            return True
        else:
            while i<len(s)-1:
                i+=1
                con(s,ch,i)
            return False

print(con('benny','e',0))
