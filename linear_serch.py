#Linear Serch
import sys

def linear_serch(numbers):
    size = len(numbers)
    print("Enter the target:",end="")
    target = int(sys.stdin.readline())
    for i  in range(0,size):
        if target == numbers[i]:
            return i
    return -1

print("Enter test case number:",end="")
t = int(sys.stdin.readline())
for _ in range(t):
    print("Enter list size:",end="")
    n = int(sys.stdin.readline())
    print("Enter number:",end="")
    nums = []
    while(len(nums) < n):
        inputes = sys.stdin.readline().split()
        if not inputes:
            continue
        for value in inputes:
            if len(nums) < n:
                nums.append(int(value))
    index = linear_serch(nums)
    print("The targeted index is:",index)