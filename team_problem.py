import sys
n = int(sys.stdin.readline())
i = 1
cou = 0
while ( i <= n):
    a,b,c = map(int,sys.stdin.readline().split())
    if (a+b+c) > 1:
        cou = cou + 1
    i += 1
print(cou)
# import sys
# n = int(sys.stdin.readline())
# if (n % 2 == 0 and n != 2):
#     print("YES")
# else:
#     print("NO")