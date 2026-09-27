'''
n = int(input())
k = 1
sum = 0
for i in range(1, n + 1):
    for j in range(1,i+1):
        sum = sum + k
        k += 1
print(sum)
'''

import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    A = list(map(int,sys.stdin.readline().split()))
    wait = 0
    time = 0 
    for c in A:
        if c < time:
            wait = wait + (time - c)
        else:
            time = c
    print(wait)