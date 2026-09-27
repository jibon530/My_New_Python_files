n = int(input())

for i in range(1, n+1):
    x = int(input())

    y = (180-x)/2
    z = (180-2*x)

    print(f"{z:.8f} {y:.8f}")