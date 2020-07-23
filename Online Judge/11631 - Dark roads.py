# Minimum spanning tree

import heapq

def read_input():
    n, m = (int(i) for i in input().split())
    if n == m == 0:
        return
    adjacent = [[] for i in range(n)]
    edges = []
    total_cost = 0
    for i in range(m):
        u, v, w = (int(j) for j in input().split())
        edges.append((w, u, v))
        total_cost += w
    edges.sort()
    return n, edges, total_cost

def find(parents, x):
    if x == parents[x]:
        return x
    return find(parents, parents[x])

def union(parents, x, y):
        a = find(parents, x)
        b = find(parents, y)
        parents[b] = a

def kruskal(edges, n):
    parents = [i for i in range(n)]
    min_cost = 0
    for (w, u, v) in edges:
        if find(parents, u) != find(parents, v):
            union(parents, u, v)
            min_cost += w
    return min_cost

if __name__ == "__main__":
    i = 0
    for n, edges, total_cost in iter(read_input, None):
        min_cost = kruskal(edges, n)
        print(total_cost - min_cost)
        i += 1
