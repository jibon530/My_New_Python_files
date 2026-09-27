import math
def cal(p,q,r):
    d = (b**2) - (4*a*c)
    if (d == 0):
        x = (-b / 2*a)
        print("The root is real and the value is: ",round(x,2))
    elif (d > 0):
        x1 = ((-b) + (math.sqrt(d))) / (2*a)
        x2 = ((-b) - (math.sqrt(d))) / (2*a)
        print("The roots are real and the value is:", round(x1,2), "and", round(x2,2))
    else:
        print("Sorry..! But the roots are not possible.")
a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))
c = float(input("Enter the third number:"))

cal(a,b,c)