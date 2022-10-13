def addOneToEverything(x,index):
    l = len(x)
    if index==l:
        return x
    else:
        x[index] = x[index]+1
        return addOneToEverything(x,(index+1))
    
print(addOneToEverything([2,6,3,8],0)) #Calling the function using the value of list and the default index number
