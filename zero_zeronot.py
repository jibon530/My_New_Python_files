import sys
def zero():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        if n == 0:
            print("The number is zero.")
        else:
            print("The number isn't zero.")
if __name__=="__main__":
    zero()