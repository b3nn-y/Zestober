import numpy as np
def checkboard(n):
    array = []
    for i in range(n):
        array.append(list(np.tile([1,2],int(n/2))) if i%2==0 else list(np.tile([2,1],int(n/2))))
    print(np.array(array))
n  = int(input("Enter a num: "))
checkboard(n)
