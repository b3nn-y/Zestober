def tri(x,y,z):
    if x+y+z == 180 and a>=1 and b>=1 and c>=1:#Since angle cant be 0!!!
        print("The given angles will construct a triangle")
    else:
        print("The given angles will not construct a triangle")

a = int(input("Enter the first angle: "))
b = int(input("Enter the second angle: "))
c = int(input("Enter the third angle: "))

tri(a,b,c)
