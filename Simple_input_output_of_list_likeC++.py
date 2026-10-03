#Largest value in a List
import sys

print("Enter test case number:",end="")
t = int(sys.stdin.readline())

for _ in range(t):

    print("Enter the list size:",end="")
    n = int(sys.stdin.readline())

    print("Enter number:",end="")
    nums = []
    while(len(nums) < n):
        inputs = sys.stdin.readline().split()
        if not inputs:
            continue
        for val in inputs:
            if len(nums) < n:
                nums.append(val)
    print("The values are: ",end="")
    #print(*nums)
    for val in nums:
        print(val,end=" ")
    print()