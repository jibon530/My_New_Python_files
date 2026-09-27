n = int(input("Enter the number: "))

f1 = 0
f2 = 1

print("The", 1, "nth fibonacci is:", f1)

if n >= 2:
    print("The", 2, "nth fibonacci is:", f2)

for i in range(3, n + 1):

    fibo = f1 + f2

    f1 = f2
    f2 = fibo

    print("The", i, "nth fibonacci is:", fibo)