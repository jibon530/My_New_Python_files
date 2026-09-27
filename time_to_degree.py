a,b = map(int,input().split())
x = (a*30)+(b*0.5)
y = (b*6)
angle = abs(x-y)
if angle > 180:
    angle -= 360
    angle = abs(angle)
else:
    angle = angle

print(f"{angle:.4f}")