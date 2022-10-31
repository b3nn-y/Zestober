def table(n):
    for i in range(1,n):
        for j in range(1,n):
            temp=0
            if i*j<n:
                temp = i*j
            else:
                temp= (i*j)%n
            print(temp,end=' ')
        print(end='\n')

n=int(input("Enter the length of the table: "))        
table(n)
        
