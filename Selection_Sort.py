import sys

def Selection_Sort(number,size):
    for i in range(0,size):
        for j in range(i+1,size):
            if(number[i] > number[j]):
                number[i],number[j] = number[j],number[i]
    return number

print("Enter the test case number:",end="")
t = int(sys.stdin.readline())
for _ in range(t):
    print("Enter the Array size:",end="")
    n = int(sys.stdin.readline())
    print(f"Enter {n} Array's value with seperate spaces:",end="")
    nums = []
    while(len(nums) < n):
        inputes = sys.stdin.readline().split()
        if not inputes:
            continue
        for value in inputes:
            if (len(nums) < n):
                nums.append(int(value))

    number = Selection_Sort(nums,n)
    for value in number:
        print(value,end=" ")
    print()