def bitFlip(s,i):
    while i<len(s):
        if s[i]=='0':
            s = s[:i] + '1' + s[i+1:]
            return bitFlip(s,i+1)
        elif s[i]=='1':
            s = s[:i] + '0' + s[i+1:]
            return bitFlip(s,i+1)
        else:
            print("Wrong Input")
            break
    return s

x=input("Enter a combination of 0&1: ")
print(bitFlip(x,0))
