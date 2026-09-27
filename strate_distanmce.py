import math
# a = int(input())
# b = int(input())
a,b = map(int,input().split())
c = math.pow(a,2) + math.pow(b,2)
ans = math.sqrt(c)
print(ans)