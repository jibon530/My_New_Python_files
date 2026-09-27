import math
r = float(input("Enter:"))
th = float(input("Enter:"))
pi = math.acos(-1)
x = r*math.cos(th*pi/180)
y = r*math.sin(th*pi/180)
print (round(x,2), " ", round(y,2))