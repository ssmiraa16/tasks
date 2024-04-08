N=int(input())
M=int(input())

list_pair=[]
counter=1

for i in range(0, M):
    list_pair.append(list(map(int, input().split(" "))))

list_pair.sort()

for i in range(0, M-1):
    if (list_pair[i][1]<=list_pair[i+1][0]):
        counter+=1

print(counter)