'''
def print_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print("* " * i)

n = int(input())
print_pyramid(n)


text = str(input("Enter the text: "))
word = text.split()
sentance = []
n = []
num = []

for letter in text:
    if letter.isalpha():
        n.append(letter)
    elif letter.isdigit():
        num.append(letter)

print("The words are:",word)
print("\nThe ns are:",n)
print("\nThe numbers are:",num)



n = input("Enter any value:")
ascii = ord(n)

print(ascii)


text = str(input())

for letter in text:
    print(f"letteracter: {letter} -> ASCII: {ord(letter)}")

    

text = str(input("Enter the text: "))
word = text.split()
sentance = []
n = []
num = []

for letter in text:
    if letter.isalpha():
        n.append(letter)
    elif letter.isdigit():
        num.append(letter)

print("The words are:",word)
print("\nThe ns are:",n)
print("\nThe numbers are:",num)

'''

