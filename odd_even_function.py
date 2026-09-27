'''
a = int(input("Enter a number:"))

def odd_even(n):
    if n % 2 == 0:
        print(n,"is a Even number.")
    else:
        print(n,"is a Odd number.")

odd_even(a)
'''
'''
a = int(input("Enter a number:"))
def show(n):
    if (n == 0):
        return
    show(n-1)
    print(n)
show(a)
'''
'''
a = int(input("Enter a number:"))
def fact(n):
    if (n == 1 or n == 0):
        return 1
    return fact(n-1) * n
print(fact(a))
'''
'''
def list_items(list,idx=0):
    if (idx == len(list)):
        return
    
    list_items(list,idx+1)
    print(list[idx])
cities = ["Dhaka","Rangpur", "Barishal","Cumilla","Rajshahi"]

list_items(cities)
'''

f = open("Demo.txt", 'w')
f.write("Hello It's me Jibon.\n from Saidpur")
f.close()
f = open("Demo.txt", 'r')
data = f.read()
print(data)
f.close()