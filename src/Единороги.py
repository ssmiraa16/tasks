N=int(input())
K=int(input())
M=int(input())
unic=0
ost=0
while N>=K:
    ost=0
    for i in range(N//K):
        unic+=K//M
        ost+=K%M
    N=ost
print(unic)