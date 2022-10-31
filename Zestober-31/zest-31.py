import random
def minesweeper(n,m):
    lst=[]
    out=['O','M']
    for i in range(n):
        temp=[]
        for i in range(m):
            a=random.choice(out)
            temp.append(a)
            print(a,end=" ")
        lst.append(temp)
        print(end=' \n')
    #print(lst)
    b=len(lst)
    print('\n')
    for i in range(len(lst)):
        c=lst[i]
        for j in range(len(c)):
            if c[j]=='O':
                count=0
                if i==0 or i==(len(lst)-1):
                    if i==0:
                        if 'M' == (lst[i+1])[j]:
                            count+=1
                    if i==(len(lst)-1):
                        if 'M' == (lst[i-1])[j]:
                            count+=1
                    if j!=0 and j!=(len(c)-1):
                        if 'M' == (lst[i])[j-1]:
                            count+=1
                        if 'M' ==(lst[i])[j+1]:
                            count+=1
                        if i!=0 and i!= (len(lst)-1):
                            if 'M' == (lst[i+1])[j+1]:
                                count+=1
                            if 'M' == (lst[i+1])[j-1]:
                                count+=1
                            if 'M' == (lst[i-1])[j+1]:
                                count+=1
                            if 'M' == (lst[i-1])[j-1]:
                                count+=1
                    if j == 0:
                        if 'M' ==(lst[i])[j+1]:
                            count+=1
                    if j==(len(c)-1):
                        if 'M' == (lst[i])[j-1]:
                            count+=1
                else:
                    if j!=0 and j!=(len(c)-1):
                        if 'M' == (lst[i])[j-1]:
                            count+=1
                        if 'M' ==(lst[i])[j+1]:
                            count+=1
                        if i!=0 and i!= (len(lst)-1):
                            if 'M' == (lst[i+1])[j+1]:
                                count+=1
                            if 'M' == (lst[i+1])[j-1]:
                                count+=1
                            if 'M' == (lst[i-1])[j+1]:
                                count+=1
                            if 'M' == (lst[i-1])[j-1]:
                                count+=1
                    if j == 0:
                        if 'M' ==(lst[i])[j+1]:
                            count+=1
                    if j==(len(c)-1):
                        if 'M' == (lst[i])[j-1]:
                            count+=1      
                print(count,end=' ')
            else:
                print(c[j],end=' ')
        print(end=' \n')           
                
minesweeper(7,5)            

