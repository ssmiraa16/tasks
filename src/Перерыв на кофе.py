A, B, P=map(int, input().split(" "))
X=0
while (B*X)%P!=A:
    X+=1
print(X)