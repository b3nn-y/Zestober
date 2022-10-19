import random
def day19(x):
    finalList=[]
    count=0
    num = [1,2,3,4,5]
    if x<=100:
        for i in range(x):
            lst = []
            for j in range(x):
                lst.append(random.choice(num))
            finalList.append(lst)
        for i in finalList:
            print(i)
        for i in finalList:
            for j in i:
                if j ==5:
                    count+=1
        print('The number of fives are-',count)
    else:
        print("Enter a number less than 100")
n=int(input("Enter a number: "))
day19(n)
    

