import math
x = float(input())
y = float (input())
r = math.sqrt((x*x)+(y*y))
th = math.atan2(y,x)
print(r,th)