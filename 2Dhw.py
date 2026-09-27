import math
r = float(input("Enter the value:"))
th = float(input("Enter the value:"))
pi = math.acos(-1)
x = r * math.cos(th*pi/180)
y = r * math.cos(th*pi/180)
print(round(x,2), round(y,2))