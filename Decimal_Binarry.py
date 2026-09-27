import sys
def deci_bin(deci):
    
    ans,pow = 0,1
    
    while (deci > 0):
        rem = deci % 2
        deci //= 2
        ans += (rem * pow)
        pow *= 10
    return ans

t = int(sys.stdin.readline())

for _ in range(t):
    num = int(sys.stdin.readline())
    print("Decimal = ", num, " Binarry = ", deci_bin(num))