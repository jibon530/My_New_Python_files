import math
n = float(input("Enter a number:"))
s = math.sqrt(n)
f = math.floor(s)
m = s - f
if m > 0.5:
    ans = f + 1
    print("The answere is:", ans)
else:
    print("The answere is:", f)