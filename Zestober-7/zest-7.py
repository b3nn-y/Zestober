def leapYear(x):
    if(x%4 == 0 and x%100!=0 ):
        print("Leap Year")
    elif(x%400 == 0 and x%100==0 ):
        print("Leap Year")
    else:
        print("Just 365 Days!!(Not a Leap Year)")
a = int(input("Enter a year: "))
leapYear(a)
