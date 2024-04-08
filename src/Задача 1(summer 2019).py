N=int(input())
start=100
min_S=start
for i in range(N):
    metres=int(input())
    start+=metres
    if (min_S>start):
        min_S=start
print(min_S)