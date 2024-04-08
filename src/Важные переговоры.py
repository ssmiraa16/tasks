N, M = map(int, input().split())
conflicts = []
for _ in range(M):
    conflicts.append(list(map(int, input().split())))
def can_seat_together(N, conflicts):
    adj_list = {i: set() for i in range(1, N+1)}
    for a, b in conflicts:
        adj_list[a].add(b)
        adj_list[b].add(a)
    visited = {}
    for i in range(1, N+1):
        if i not in visited:
            visited[i] = 1
            stack = [i]
            while stack:
                node = stack.pop()
                for neighbor in adj_list[node]:
                    if neighbor in visited:
                        if visited[neighbor] == visited[node]:
                            return "NO"
                    else:
                        visited[neighbor] = 3 - visited[node]
                        stack.append(neighbor)

    return "YES"

print(can_seat_together(N, conflicts))