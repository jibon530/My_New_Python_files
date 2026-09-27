import math
a,b,c = map(float,input().split())
if (a+b)>c and (b+c)>a and (a+c)>b:
    s = (a+b+c)/2
    pi = math.acos(-1)
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    th = (math.asin((2*area)/(a*b))*(180/pi))
    bi = (math.asin((2*area)/(a*c))*(180/pi))
    al = (math.asin((2*area)/(b*c))*(180/pi))
    print("The answere is:", round(th,2) , round(bi,2) , round(al,2))
    print(round(area,2))
else:
    print("Traingle is not possible..!")