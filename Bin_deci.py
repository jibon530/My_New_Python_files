import sys

def bin_deci(bin):

    ans,power = 0,1

    while(bin > 0):
        rem = bin % 10
        ans += (rem * power)
        bin //= 10
        power *= 2
    return ans

t = int(sys.stdin.readline())

for _ in range(t):
    num = int(sys.stdin.readline())
    print("Binarry =",num,"Decimal =",bin_deci(num))
