'''
import sys
a,b = map(int,sys.stdin.readline().split())
lcm = a * b
while b != 0:
    a,b = b,a % b
gcd = a
lcm = lcm // gcd
print("The LMC is:",lcm,"\nThe GCD is:",gcd)


a = int(input())
b = int(input())

num1, num2 = a, b 

while b > 0:
    a, b = b, a % b

gcd = a
lcm = (num1 * num2) // gcd

print("The GCD is: ",gcd,"\nThe LCM is: ",lcm)

import sys
a, b = map(int, sys.stdin.readline().split())

lcm = a * b
while b != 0:
    a, b = b, a % b 

gcd = a
lcm = lcm // gcd

print("The LCM is:", lcm, "\nThe GCD is:", gcd)


import sys
import math
a,b = map(int,sys.stdin.readline().split())
lcm = math.lcm(a,b)
gcd = math.gcd(a,b)
print(lcm, gcd)
'''
import math
num = [12,18,24,36,42]
gcd = math.gcd(*num)
lcm = math.lcm(*num)
print(gcd,lcm)