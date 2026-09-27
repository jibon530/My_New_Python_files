'''
import math
a = float(input("Enter the value of first number:"))
b = float(input("Enter the value of second number:"))
c = float(input("Enter the value of third number:"))

d = (b**2)-(4*a*c)

if (d > 0):
    x1 = ((-b + math.sqrt(d)))/ (2*a)
    x2 = ((-b - math.sqrt(d))/ (2*a))
    print("The roots are real and not equal:", x1, x2)
elif (d==0):
    x = -b / (2*a)
    print("The root is:", x)
else:
    print("Sorry..! The roots are not possible..")

'''

n = input("Enter what you want to write:")
num = int(input("Enter how many times you want to write:"))

for i in range(1,num+1):
    print(n,i)