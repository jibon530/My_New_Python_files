import sys
a,b,c = map(float,sys.stdin.readline().split())
if (a > b and a > c):
    print("Largest number is: ", a)
elif (b > c):
    print("Largest number is: ", b)
else:
    print("Largest number is: ", c)