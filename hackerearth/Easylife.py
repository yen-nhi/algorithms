from fractions import Fraction

def dfs(adjacent, v, visited):
    stack = [v]
    visited[v] = True
    vertices = 1
    edges = 0
    while stack:
        u = stack.pop()
        for v in adjacent[u]:
            edges += 1
            if not visited[v]:
                stack.append(v)
                visited[v] = True
                vertices += 1
    return Fraction(edges/2/vertices)

def easylife(adjacent, n):
    visited = [False] * n
    maximal = 0
    for v in range(n):
        if not visited[v]:
            maximal = max(maximal, dfs(adjacent, v, visited))
    return maximal

n, m = map(int, input().split())
if m == 0:
    print('0/1')
else:
    adjacent = [[] for i in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        adjacent[u-1].append(v-1)
        adjacent[v-1].append(u-1)
    density = easylife(adjacent, n)
    if density > 1:
        print('>1')
    elif density == 1:
        print('1/1')
    else:
        print(Fraction.limit_denominator(density))