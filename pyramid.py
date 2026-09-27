'''
import sys
n = int(sys.stdin.readline())
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print(" ")
    
    

import sys
n = int(sys.stdin.readline())
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print(" ")

 
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(2*i -1):
        print("*",end="")
    print()

    
    n = int(input())

for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()
    

n = int(input())
a = 0
b = 1
i = 1
ans = 1
print(a,b,end=" ")
while(i < n):
    ans = a + b
    a = b
    b = ans
    print(ans,end=" ")
    i += 1


# import math

# n = int(input())
# if n <= 1:
#     prime = False
# else:
#     prime = True
#     for i in range(2, int(math.isqrt(n)) + 1):
#         if n % i == 0:
#             prime = False 
#             break          
# if prime == True:
#     print(n,"is a prime number..")
# else:
#     print(n,"isn't a prime number..")
'''
n = int(input())
prime = False
for i in range(2,n):
    if (n % i == 0):
        prime = True
        break
if (prime == True):
    print("Not Prime..")
else:
    print("Prime..")