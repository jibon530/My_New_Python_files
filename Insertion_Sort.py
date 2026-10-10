import sys

def Insertion_Sort(numbers,size):
    for i in range(1,size):
        x = numbers[i]
        j = i - 1
        while(j >= 0 and numbers[j] > x):
            numbers[j+1] = numbers[j] 
            j -= 1
        numbers[j+1] = x

    return numbers

print("Enter test case number:",end="")
t = int(sys.stdin.readline())

for _ in range(t):

    print("Enter Array Size:",end="")
    n = int(sys.stdin.readline())
    print("Enter the numbers:",end="")
    nums = []

    while(len(nums) < n):
        inputes = sys.stdin.readline().split()
        if not inputes:
            continue
        for value in inputes:
            if(len(nums) < n):
                nums.append(int(value))

    New_nums = Insertion_Sort(nums,n)

    # print("The sorted values are:",*New_nums)
    for value in New_nums:
        print(value,end=" ")
    print()