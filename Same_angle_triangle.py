import sys

def area(base,height):

    return (0.5 * base * height)

t = int(sys.stdin.readline())

for _ in range(t):
    
    a,b,c = map(float,sys.stdin.readline().split())

    if(a*a + b*b == c*c):
        print("This is a valid Triangle.")
        print(f"The area of the triangle = {area(a,c):.2f}")
    else:
        print("Sorry..!But invalid triangle.")