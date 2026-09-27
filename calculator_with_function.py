print("1.Addition")
print("2.Subtraction.")
print("3.Multiplication.")
print("4.Divition.")
n = int(input("Enter number only like 1,2,3,4\nEnter: "))
def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul (x,y):
    return x * y
def div (x,y):
    if (y != 0):
        return x / y
    else:
        return "Sorry...! But the divition is not possible."
# a = float(input("Enter the first value: "))
# b = float(input("Enter the second value: "))
if n == 1:
    a = float(input("Enter the first value: "))
    b = float(input("Enter the second value: "))
    print("The Addition is:",add(a,b))
elif n == 2:
    a = float(input("Enter the first value: "))
    b = float(input("Enter the second value: "))
    print("The Subtraction is: ", sub(a,b))
elif n == 3:
    a = float(input("Enter the first value: "))
    b = float(input("Enter the second value: "))
    print("The Multliplication is: ", mul(a,b))
elif n == 4:
    a = float(input("Enter the first value: "))
    b = float(input("Enter the second value: "))
    print("The Divition is: ", div(a,b))
else:
    print("Sorry..! You select the wrong option. Please, enter 1-4.")