n = int(input("Enter the number: "))
def fact(z):
    add = 1
    for i in range(1,z+1):
        add *= i*i
    return add
print("The Factrial is:",fact(n))