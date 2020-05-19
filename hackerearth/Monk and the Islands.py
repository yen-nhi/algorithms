# Bread First Search Algorithms

from collections import deque

def bfs(vertices, start, dest):
    q = deque([start])
    level = [None] * (n+1)
    level[start] = 0
    while q:
        u = q.popleft()
        for v in vertices[u]:
            if level[v] is None:
                level[v] = level[u] + 1
                q.append(v)
    return level[dest]

for t in range(int(input())):
    n, m = map(int, input().split())
    vertices = [[] for i in range(n+1)]
    for i in range(m):
        u, v = map(int, input().split())
        vertices[u].append(v)
        vertices[v].append(u)
    print(bfs(vertices, 1, n))

