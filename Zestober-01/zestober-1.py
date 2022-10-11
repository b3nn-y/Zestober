#Challenge posted on Zoho Connect
def seizeThoseFours(x):
    countOfLength = 0
    c =x
    countOfFour = 0
    while c>1:
        c = c/10
        countOfLength+=1
    for i in range(countOfLength):
        countOfLength -=1
        a = int(x/10**countOfLength)
        if a == 4:
            countOfFour += 1
        x = x - a * 10**countOfLength
    return countOfFour 

#Challenge posted on Whatsapp 
    
def Ram():
    for i in range(1,101):
        if i % 3 ==0 and i % 5 == 0:
            print("RamRahim")
        elif i%5==0:
            print("Rahim")
        elif i%3 == 0:
            print("Ram")
        else:
            print(i)

import time
print("Hi,This is the first project of Zestober,done by-Benny Samuel")
time.sleep(1)
print("I saw 2 different challenges being posted one on the whatsapp group and a another one on zoho connect")
time.sleep(1)
print("And decided to do both as a challenge")
time.sleep(1)
print("So here we gooooo")
time.sleep(1)

print("Enter - 1(For counting the number of fours without using str())")
a = int(input("Enter-2(For the prog-If a num is a multiple of 3 or 5 print few specific names: "))
if a == 1:
    b = int(input("Enter any num: "))
    print(f"The num of 4 in {b} are: ",seizeThoseFours(b))
elif a ==2:
    Ram()
else:
    print("Wrong Input")
    
              



              
