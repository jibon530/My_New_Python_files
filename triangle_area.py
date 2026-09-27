import math
a,b,c = map(float,input().split())
if (a+b)>c and (b+c)>a and (a+c)>b:
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("The area of the triangle is:", round(area,2))
else:
    print("Sorry...! But we can't make a triangle from these values.Please enter valid values.")