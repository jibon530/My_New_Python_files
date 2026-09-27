'''
x,n = map(int,input().split())
sum = 0
for i in range(0,n+1,2):
    fact = 1
    for j in range(1,i+1,1):
        fact = fact * j
    if i % 4 == 0:
        sum = sum + ((x**i)/fact)
    else:
        sum = sum - ((x**i)/fact)
print(sum)
'''

x, n = map(int, input("Enter x and n: ").split())
ps = 1
ns = 0
for j in range(2, n + 1, 2):
    fact = 1
    for i in range(1, j + 1):
        fact = fact * i 
    term = (x ** j) / fact

    if j % 4 == 0:
        ps = ps + term
    else:
        ns = ns + term
ans = ps - ns
print("The answere is:", round(ans,))