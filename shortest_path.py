import math
import sys
def path():
    t = int(sys.stdin.readline())
    for _ in range (t):
        a,b = map(int,sys.stdin.readline().split())
        z = pow(a,2) + pow(b,2)
        ans = math.sqrt(z)
        print(f"{ans:.9f}")
if __name__ == "__main__":
    path()