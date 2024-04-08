def dfs(graph, u, visited, pairing):
    for v in range(len(graph[u])):
        if not visited[v] and graph[u][v]:
            visited[v] = True
            if pairing[v] == -1 or dfs(graph, pairing[v], visited, pairing):
                pairing[v] = u
                return True
    return False
def max_matching(graph):
    n = len(graph)
    m = len(graph[0])
    pairing = [-1] * m
    matchings = 0
    for u in range(n):
        visited = [False] * m
        if dfs(graph, u, visited, pairing):
            matchings += 1
    return matchings

graph = [[1, 0, 0],
         [0, 1, 1],
         [0, 1, 0]]
matchings = max_matching(graph)
print("Максимальное паросочетание:", matchings)