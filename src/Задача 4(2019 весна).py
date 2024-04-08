def dfs(vertex, visited, count):
    visited[vertex] = True
    count[vertex] += 1
    for neighbor in adj_list[vertex]:
        if not visited[neighbor]:
            dfs(neighbor, visited, count)


N=int(input())
matrix=[]

for i in range(0, N):
    matrix.append(list(map(str, "".join(input()))))

for i in range(0, N-1):
    for j in range(0, N-1):
        if matrix[i][j]==".":
            matrix[i][j]=1
        elif matrix[i][j]=="*":
            matrix[i][j]=0

adj_list = {}

for i in range(len(matrix)):
    adj_list[i] = []
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            adj_list[i].append(j)

count = [0] * len(matrix)
for i in range(len(matrix)):
    visited = [False] * len(matrix)
    dfs(i, visited, count)

counter=0
for neighbors in adj_list.values():
    counter+=len(neighbors)
print(counter)