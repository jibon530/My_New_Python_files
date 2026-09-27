# import sys
# a,b = map(int,sys.stdin.readline().split())
# i = 1
# for i in range(1,a+1,1):
#     if i == b:
#         break
#     print(i, end=" ")
# import sys
# a,b = map(int,sys.stdin.readline().split())
# i = 1
# for i in range (i, a+1, 1):
#     if i == b:
#         continue
#     print(i, end=" ")
import sys
a,b = map(int,sys.stdin.readline().split())
i = 1
while (i <= a):
    if i == b:
        break
    print(i, end=" ")
    i += 1