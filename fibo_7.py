'''
n = int(input())
f1 = 0
f2 = 1
for i in range(1,n+1):
    fibo = f1 + f2
    f1,f2 = f2, fibo
print(fibo)
'''
n = int(input())
num = []
add = 0
for i in range(0,n):
    a = int(input())
    num.insert(i,a)
for j in range(0,n):
    print(num[j],end=" ")
for k in range(0,n):
    add = add + num[k]
print("\n","The addition is:",add)