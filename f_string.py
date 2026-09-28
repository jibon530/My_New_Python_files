#Simple Variable
name = "Jibon"
age = 18

print(f"My name is {name} and I am {age} years old.")

#Calculation
a = 15
b = 25

print(f"Sum:{a} + {b} = {a+b}")

#Decimal fixed digit show
x = 3.1415926

print(f"{x:.4f}")                       #f"{(Variable):.(digit)} // Ignore () on this Exaample.

#Large Number with comma

n = 1000000

print(f"{n:,}")

#For Parcentage

x = 0.8745

print(f"{x:.2%}")                       #For parcentage

#Binarry, Octal, Hexadecimal

n = 45

print(f"Binarry Number\t\t= {n:b}")     #For binarry Number
print(f"Octal Number\t\t= {n:o}")       #For Octal Number
print(f"HexaDecimal number\t= {n:x}")   #For HexaDecimal Number

#Leading Zero

n = 7

print(f"{n:03}")

#sep

print(10,20,30, sep="+")                #On this + position we can apply any symbol or anything like(_,*,# anything)

#join()

a = [10,20,30,40]

print(*a)                               #By Adding (*) print function will ignore the squre braket

a = ["10","20","30","40"]

print("*".join(a))                      #On this * position we can use any symbol,But it will only work on string list.