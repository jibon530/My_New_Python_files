import sys

def Peak(numbers,size):
    low,high = 1, size - 2

    while(low <= high):
        mid = int(low + ((high - low) / 2))

        if(numbers[mid - 1] < numbers[mid] and numbers[mid] > numbers[mid+1]):
            print(f"Peak Index is: {mid} \nPeak value is: {numbers[mid]} ")
            break
        elif(numbers[mid-1] < numbers[mid]):
            low = mid + 1
        elif(numbers[mid - 1] > numbers[mid]):
            high = mid - 1
        else:
            print(f"Oops..! It's not a Mountain Array.")


print("Enter the test tase number:",end="")
t = int(sys.stdin.readline())
for _ in range(t):
    print("Enter the Mountain Array size:",end="")
    n = int(sys.stdin.readline())
    print(f"Enter {n} Mountain Array's value with seperate spaces:",end="")
    nums = []
    while(len(nums) < n):
        inputes = sys.stdin.readline().split()
        if not inputes:
            continue
        for value in inputes:
            if(len(nums) < n):
                nums.append(int(value))

    Peak(nums,n)