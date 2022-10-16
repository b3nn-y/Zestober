def ounceToPounds(x):
    p=x//16
    o=x%16
    print(f'{p} pounds and {o} ounces')

ounce=int(input("Enter the weight in ounces: "))
ounceToPounds(ounce)
