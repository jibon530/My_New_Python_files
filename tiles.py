import sys
n,m,a = map(int,sys.stdin.readline().split())
c = n // a
d = m // a
if (n % a != 0):
    c += 1
if (m % a != 0):
    d += 1
answer = c * d
print(answer)
# import sys
# n = int(sys.stdin.readline())
# answer = n * 31
# print(answer)
# import sys
# n = int(sys.stdin.readline())
# s = 0
# i = 0
# if n > 0:
#     for i in range (0,n + 1):
#         s = s + i
# else:
#     for i in range (1, n - 1, - 1):
#         s = s + i
# print(s)