'''
import sys
import math
n = int(sys.stdin.readline())
pr = []
np = []
for i in range(3,n+1,2):
    prime = True
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            prime = False
            break
    if prime == True:
        pr.append(i)
    else:
        np.append(i)
print(" #_All prime numbers for odd number...\n2 is only prime number which is even\nThat's why we count only odd numbers..")
print("Prime Numbers:", pr, "\nNot Prime Numbers:", np)


import sys
import math
n = int(sys.stdin.readline())
pr = []
np = []
for i in range(2,n+1):
    prime = True
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            prime = False
            break
    if prime == True:
        pr.append(i)
    else:
        np.append(i)

print("Prime Numbers:", pr, "\nNot Prime Numbers:", np)
'''
'''
n = int(input())
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)
'''
#Home_work
'''
import sys
n,r = map(int,sys.stdin.readline().split())
d = n - r
f1 = 1
f2 = 1
f3 = 1
for i in range(1, n+1):
    f1 = f1 * i
for i in range(1, r+1):
    f2 = f2 * i
for i in range(1, d+1):
    f3 = f3 * i
ans = int(f1 / (f2* f3))
print(ans)


import math
import sys
a,b,c = map(float,sys.stdin.readline().split())
if (a+b>c) and (b+c>a) and (a+c>b):
    s = (a+b+c)/ 2
    ans = math.sqrt((s*(s-a)*(s-b)*(s-c)))
    print("The area is the triangle is:", ans)
else:
    print("Sorry the traingle is not possible..")
'''
import math
import sys
a,b,c = map(float,sys.stdin.readline().split())
d = (b**2)-4*a*c
if d > 0:
    x1 = ((-b + math.sqrt(d)) / 2*a)
    x2 = ((-b - math.sqrt(d)) / 2*a)
    print("The roots are not equal and real:", x1 ,x2)
elif(d == 0):
    x = (-b / (2 * a))
    print("The roots are equal and real:", x)
else:
    print("The roots are imegenary")