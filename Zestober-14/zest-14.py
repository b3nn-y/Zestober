def abcd():
    letters= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    output= ""
    count=0
    c=1
    while c<=26:
        for i in letters:
            output+=i
        print(c,output)
        c+=1
        output=""
        a=letters.pop(count)
        letters.append(a)
    
abcd()
