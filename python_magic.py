'''
# 
n = int(input("Must be Even number:"))
print("Even" if n % 2 == 0 else "Odd")
for i in range(n):
    for j in range(n):
        if (i == 0 or i == n - 1 or j == 0 or j == n - 1):
            print("*", end='')
        elif(i == j or i + j == n - 1):
            print("*",end="")
        else:
            print(" ", end="")
    print()
        # 
n = 5
for i in range(n):
    for j in range(2*n-1):
        if(i == 0 or i == n-1 or j == 0 or j ==2*n-2 or i+j==n-1 or i-j==n-1+n):
            print("*",end=" ")
        else:
            print(" ",end="")
    print()

'''

import turtle
import colorsys
import math

def draw_vortex_effect():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Chromospheric")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    screen.tracer(2, 0)
    
    hue = 0.0
    iterations = 400
    magic_angle = 222

    try:
        for i in range(iterations):
            color = colorsys.hsv_to_rgb(hue, 0.9, 1)
            t.pencolor(color)
            
            hue += 1 / iterations
            width = (math.sin(i * 0.05) * 2) + 3
            t.width(width)
            
            t.forward(i * 1.5)
            t.left(magic_angle)
            t.circle(i, 90)
            t.right(45)
    except turtle.Terminated:
        print("Drawing window closed by user.")
    screen.mainloop()

draw_vortex_effect()


'''

import calendar

year = int(input("Enter  the year: "))
month = int(input("Enter the month: "))

print("\n", calendar.month(year,month))
'''