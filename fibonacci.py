n = int(input())
if n == 1 or n ==2:
    print(1)
else:
    f1 = 1
    f2 = 1
    fibo = 1
    i = 3
    while i <= n:
        fibo = f1 + f2
        f1 = f2
        f2 = fibo
        i = i + 1
print(fibo)