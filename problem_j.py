import sys
def angle():
    t = int(sys.stdin.readline())
    a = list(map(int,sys.stdin.readline().split()))
    a = sum(a)
    if (a ==((t - 2) * 180)):
        print("YES")
    else:
        print("NO")
if __name__ == "__main__":
    angle()