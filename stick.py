import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n+1]]
    arr.sort()
    
    i = 0 
    for j in range(1, n):
        
        if arr[i] <= arr[j] // 2:
            i += 1  
    ans = n - i
    print(ans)

if __name__ == '__main__':
    main()
    