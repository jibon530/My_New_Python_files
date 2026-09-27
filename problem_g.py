import math
import sys
def solve():
    n = int(sys.stdin.readline())
    for _ in range(n):
        a,b = map(int,sys.stdin.readline().split())
        x = (math.pow(a,2) + math.pow(b,2))
        ans = math.sqrt(x)
        print(f"{ans:.9f}")
# if __name__ == "__main__":
#     solve()
if __name__ == "__main__":
    solve()