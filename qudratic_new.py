import math
import sys
a,b,c = map(float,sys.stdin.readline().split())
m = -b / (2 * a)
d = pow(m,2) - (c/a)
if d < 0:
    print("Sorry...! But The Roots are Imaginary..")
elif d == 0:
    print("The roots are equal and real:",m)
else:
    u = math.sqrt(d)
    x1 = m - u
    x2 = m + u
    print("The roots are not equal and real:",x1, x2)