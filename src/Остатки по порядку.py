M = int(input())
remainders = [int(input()) for _ in range(M-1)]

N = 1
found = False

while not found:
    found = True
    for i in range(2, M+1):
        if N % i != remainders[i-2]:
            found = False
            break
    N += 1

print(N-1)