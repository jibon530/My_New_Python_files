import sys

def solve():
    line = sys.stdin.readline().strip()
    if not line:
        return
    num = int(line)
    
    
    if num >= 20:
        print("0000")
        return
        
    
    fact = 1
    for i in range(1, num + 1):
        fact *= i
        
    ans = fact % 10000
    
    
    print(ans)

if __name__ == "__main__":
    solve()