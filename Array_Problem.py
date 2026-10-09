import sys

def find_1(numbers):
    count,max_count,size =0,0,len(numbers)
    for i in range(0,size):
        if(numbers[i] == 1):
            count += 1
            max_count = max(count,max_count)
        else:
            count = 0
    return max_count

print("Enter the test case number:",end="")
t = int(sys.stdin.readline())
for _ in range(t):
    print("Enter the List size:",end="")
    n = int(sys.stdin.readline())
    print("Enter the number:",end="")
    nums = []
    while(len(nums) < n):
        inputs = sys.stdin.readline().split()
        if not inputs:
            continue
        for value in inputs:
            if (len(nums) < n):
                nums.append(int(value))

    max_1 = find_1(nums)
    print(f"The max 1 repert is: {max_1} times.")