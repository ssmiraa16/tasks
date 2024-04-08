N=int(input())
arr=[0*i for i in range(0, N)]
counter=0
for i in range(0, N):
    arr[i]=list(map(int, input().split(" ")))
for i in range(0, N-1):
    for j in range(0, N-1):
        if (((arr[i][j]==1) and (arr[i][j+1]==1)) or ((arr[i][j]==1) and (arr[i][j-1]==1))):
            counter+=1

print(counter)