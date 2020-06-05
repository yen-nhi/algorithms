from collections import deque

def bfs(graph, u, distances):
    q = deque([u])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if distances[u] + 1 < distances[v]:
                distances[v] = distances[u] + 1
                q.append(v)   

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
distances = [float('inf')] * (n+1)
distances[1] = 0
for i in range(m):
    query = [int(i) for i in input().split()]
    if query[0] == 1:   
        res = distances[query[1]]
        if res == float('inf'):
            print(-1)
        else:
            print(res)
    elif query[0] == 2:
        u, v = query[1], query[2]
        graph[u].append(v)
        bfs(graph, u,distances)

