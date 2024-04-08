N=int(input())

x_points=[]
y_points=[]

for i in range(0, N):
    temp_x, temp_y=map(float, input().split(" "))
    x_points.append(temp_x)
    y_points.append(temp_y)

x, y=map(float, input().split(" "))

def inPolygon(x, y, xp, yp):
    c=0
    for i in range(len(xp)):
        if (((yp[i]<=y and y<yp[i-1]) or (yp[i-1]<=y and y<yp[i])) and
            (x > (xp[i-1] - xp[i]) * (y - yp[i]) / (yp[i-1] - yp[i]) + xp[i])):
            c = 1 - c
    return c

if (inPolygon(x, y, x_points, y_points)==1):
    print("YES")
else:
    print("NO")