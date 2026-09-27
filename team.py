import sys

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    t = int(input_data[0])
    
    results = []
    for i in range(1, t + 1):
        n = int(input_data[i])
        
       
        if n % 2 == 0:
            half = n // 2
            ans = half * half
            
        else:
            if n == 1:
                ans = 0
            elif n == 3:
                ans = 1
            else:
                team_a = (n + 3) // 2
                team_b = (n - 3) // 2
                ans = team_a * team_b
                
        results.append(str(ans))
        
    print('\n'.join(results))

if __name__ == '__main__':
    main()