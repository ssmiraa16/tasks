N=int(input())

counter=0
elevators=[]

for i in range(0, N):
    start, finish=map(int, input().split(" "))
    elevators.append((start, finish))
    i+=1

elev_sorted=sorted(elevators, key=lambda x: x[0] and x[1])

min_floor=elev_sorted[0]
elev_sorted.remove(min_floor)
counter+=1

def find(arr, cond, value):
    for el in arr:
        if cond(value, el):
            return el
    return None

def conditional(lhs, rhs):
    return lhs[1]==rhs[0]

while True:
    first=find(elev_sorted, conditional, min_floor)
    if first:
        counter+=1
        min_floor=first
        elev_sorted.remove(min_floor)
    else:
        break

print(counter)