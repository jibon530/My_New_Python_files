import sys
import math

def Equilateral():

    print("Enter the Equilateral triangle side:",end="")

    a = float(sys.stdin.readline())

    area = (math.sqrt(3) / 4) * (a * a)

    print(f"The area of Equilateral Triangle is:{area:.3f}")

def Isosceles():

    print("Enter the same side and other side with seperate spaces:",end="")

    a,b = map(float,sys.stdin.readline().split())

    area = (a / 4) * math.sqrt((4 * (b*b)) - (a*a))

    print(f"The area of Isosceles Triangle is:{area:.3f}")

def Scalen():

    print("Enter the three triangle side with seperate spaces:",end="")

    a,b,c = map(float,sys.stdin.readline().split())

    if((a+b) > c and (b+c) > a and (a+c) > b):

        s = a + b + c

        area = math.sqrt(s*(s-a)*(s-b)*(s-c))

        print(f"The area of Scalen Triangle is:{area:.3f}")
    else:
        print("Sorry..!But invalid triangle.")

print("Enter the test case number:",end="")

t = int(sys.stdin.readline())

for _ in range(t):

    print("01.Equilateral Triangle.")
    
    print("02.Isosceles Triangle.")
    
    print("03.Scalen Triangle.")
    
    option = int(input("Chose only one option:"))

    if (option == 1):
        Equilateral()
    elif(option == 2):
        Isosceles()
    elif(option == 3):
        Scalen()
    else:
        print("Sorry..!Please chose a valid option.")