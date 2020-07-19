# Topological Sort

import sys
sys.setrecursionlimit(1000000)

def read_input():
    n, m = map(int, input().split())
    graph = [[] for i in range(n)]
    for j in range(m):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
    return graph, n

def dfs(graph, v, visited, order):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(graph, u, visited, order)
    order.append(v)

def dominos_falls(graph, n):
    visited = [False] * n
    order = []
    for v in range(n):
        if not visited[v]:
            dfs(graph, v, visited, order)
    visited = [False] * n
    count = 0
    while order:
        v = order.pop()
        if not visited[v]:
            dfs(graph, v, visited, [])
            count += 1
    return count
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        graph, n = read_input()
        print(dominos_falls(graph, n))
        