import sys

def Palindrom(n):
    n1,reverse = n,0
    while(n > 0):
        rem = n % 10
        reverse = (reverse * 10) + rem
        n //= 10
    
    if(reverse == n1):
        print("Palindrom")
    else:
        print("Not Palindrom")

t = int(sys.stdin.readline())

for _ in range(t):
    
    num = int(sys.stdin.readline())
    
    Palindrom(num)