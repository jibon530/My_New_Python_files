import sys

def Insertion_Sort(number,size):
    for i in range(1,size):
        x = nums[i]
        j = i - 1
        while(j >= 0 and number[j] > x):
            number[j+1] = number[j]
            j -= 1
        number[j+1] = x
    return number

def Binarray_Search(numbers,n,x):

    numbers = Insertion_Sort(numbers,n)

    # print("The new sorted array is:", *numbers)
    print("The new sorted array is:",end="")
    for value in numbers:
        print(value,end=" ")
    print()
    low,high = 0, n-1
    while(low <= high):
        mid = int(low + (high - low) / 2)
        if( numbers[mid] == x):
            return mid
        elif(numbers[mid] < x):
            low = mid + 1
        else:
            high = mid - 1
    return -1

print("Enter the test case number:",end="")
t = int(sys.stdin.readline())
for _  in range(t):
    print("Enter the Array size:",end="")
    n =  int(sys.stdin.readline())
    print("Enter the Array's value with seperate spaces:",end="")
    nums = []
    while(len(nums) < n):
        inputes =  sys.stdin.readline().split()
        if not inputes:
            continue
        for value in inputes:
            if (len(nums) < n):
                nums.append(int(value))

    print("Enter the targeted value:",end="")
    target = int(sys.stdin.readline())
    print(f"The targeted index is: {Binarray_Search(nums,n,target)}")