x1, y1, x2, y2=map(int, input().split(" "))
x3, y3, x4, y4=map(int, input().split(" "))

x_min=10
x_max=0
y_min=10
y_max=0

for i in x1, x2, x3, x4:
    if i<x_min:
        x_min=i
    elif i>x_max:
        x_max=i

for j in y1, y2, y3, y4:
    if j<y_min:
        j_min=i
    elif j>y_max:
        y_max=j

new_x=x_max-x_min
new_y=y_max-y_min

if new_x>new_y:
    S=new_x**2
elif new_y>new_x:
    S=new_y**2

print(S)