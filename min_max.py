n = int(input())

for i in range(1, n+1):
    x = float(input())
    y = (180 - x)/2
    z = (180 - 2*x)
    print(f"{z:.9f} {y:.9f}")

# n = int(input())
# for i in range (1, n+1):
#     a = int(input())