N, M=map(int, input().split(" "))
matrix=[]

for i in range(N):
    matrix.append(list(map(int, input().split(" "))))

counter1=0
counter2=0

for i in range(0, N):
    counter1+=matrix[i][i]
    counter2+=matrix[i][N-i-1]

print(max(counter2, counter1))