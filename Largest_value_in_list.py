#Largest value
import sys
print("Enter the test case number:",end="")
t = int(sys.stdin.readline())
for _ in range(t):
    print("Enter the list size:",end="")
    n = int(sys.stdin.readline())
    print("Enter the number:",end="")
    nums = []
    while(len(nums) < n):
        inputes = sys.stdin.readline().split()
        if not inputes:
            continue
        for value in inputes:
            if len(nums) < n:
                nums.append(float(value))
    # largest_value = max(nums)
    # print("The maximum value is:", largest_value)
    largest_value = nums[0]
    for value in nums:
        if largest_value < value:
            largest_value = value
    print("The largest value is:",largest_value)