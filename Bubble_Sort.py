import sys

def Bubble_Sort(number,size):

    for i in range(1,size+1):
        for j in range(0,size - i):
            if(number[j] > number[j+1]):
                number[j],number[j+1] = number[j+1],number[j]

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
            if(len(nums) < n):
                nums.append(int(value))
    numbers = Bubble_Sort(nums,n)
    print("The sortedd Array is:",end="")
    for value in numbers:
        print(value,end=" ")
    print()