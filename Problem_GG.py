n = int(input())

a = list(map(int, input().split()))

a.sort()

i = 0
j = (n+1)//2

paired = 0

while i<n//2 and j<n:
    if a[i]*2<=a[j]:
        paired += 1
        i += 1
        j += 1
    else:
        j +=1

print(n - paired)