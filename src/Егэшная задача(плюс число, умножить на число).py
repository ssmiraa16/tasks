x, y=map(int, input().split(" "))

steps_count = 0
while y > 0 and y != x:
    if y % 4 == 0 and y / 4 >= x:
        y = y / 4
        steps_count += 1
    else:
        y -= 3
        steps_count += 1

if y <= 0:
    print(-1)
else:
    print(steps_count)