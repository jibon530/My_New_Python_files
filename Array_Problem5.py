import sys

def Addition(numbers,p,q):

    total = 0
    while(p <= q):
        total += numbers[p]
        p += 1
    return total


print("Enter the Array size:",end="")
n = int(sys.stdin.readline())

print("Enter the Array values:",end="")
nums = []
while(len(nums) < n):
    inputes = sys.stdin.readline().split()
    if not inputes:
        continue
    for value in inputes:
        if(len(nums) < n):
            nums.append(int(value))

print("Enter the test case number:",end="")   
t = int(sys.stdin.readline())
for _ in range(t):

    print("Enter i and j index number with seperate spaces:",end="")

    i,j = map(int,sys.stdin.readline().split())

    sumation = Addition(nums,i,j)

    print(f"The Sumation of {i} to {j} index is: {sumation} ")