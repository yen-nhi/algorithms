# Bread First Search Algorithms
from collections import deque

def minimum_flight(vertices, start, dest):
    number = [None] * (len(vertices))
    prev = [None] * (len(vertices))
    number[start] = 1
    q = deque([start])
    while q:
        u = q.popleft()
        for v in vertices[u]:
            if number[v] is None:
                number[v] = number[u] + 1
                q.append(v)
                prev[v] = u
            if v == dest:
                route = [v]
                while prev[route[-1]] is not None:
                    route.append(prev[route[-1]])
                route.reverse()
                return number[v], route
    return 1, [start]

n, m, t, c = map(int, input().split())
vertices = [[] for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    vertices[x].append(y)
    vertices[y].append(x)
for points in vertices:
    points.sort()
start, dest = map(int, input().split())

number_of_flight, route = minimum_flight(vertices, start, dest)
print(number_of_flight)
print(*route)