n = int(input())
n1 = n
reverse = 0
while (n != 0):
    reminder = n % 10
    reverse = (reverse * 10) + reminder
    n = n // 10
print(reverse)
if n1 == reverse:
    print("Palindrom")
else:
    print("Not Palindrom")