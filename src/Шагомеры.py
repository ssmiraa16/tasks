x, y=map(int, input().split(" "))
days=0

while x<y:
    x*=1.7
    days+=1

print(days)