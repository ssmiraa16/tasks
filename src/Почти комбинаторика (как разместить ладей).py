N, K=map(int, input().split(" "))
res=1
if N==K:
    for i in range(1, N+1):
        res*=i
else:

    for i in range(N, N-K, -1):
        res*=i**2
    for i in range(2, K+1):
        res//=i

print(res)