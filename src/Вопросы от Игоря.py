N, q=map(int, input().split(" "))
arr=list(map(int, input().split(" ")))
max_arr=[]
for i in range(q):
    l, r=map(int, input().split(" "))
    l-=1
    r-=1
    max_arr.append(max(arr[l:r+1]))

print(*max_arr)