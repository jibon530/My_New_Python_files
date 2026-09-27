# import sys
# n = int(sys.stdin.readline())
# i = 1
# answer = 0
# while ( i <= n):
#     a = list(map(int,sys.stdin.readline().split()))
#     s = sum(a)
#     if ( s >= 2):
#         answer = answer + 1
#     i +=1
# print(answer)

import sys
n,m,a = map(int,sys.stdin.readline().split())
x = n // a
y = m // a
if (n % a != 0):
    x += 1
if (m % a != 0):
    y += 1
ans = x * y
print(ans)