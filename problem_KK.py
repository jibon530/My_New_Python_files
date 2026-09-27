import sys
def flower():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = ((n+1)//2)
        b = ((n-1)//2)
        print(a,b)
if __name__== "__main__":
    flower()