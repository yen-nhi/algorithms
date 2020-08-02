
import math
import heapq

def read_input():
    s, n = map(int, input().split())
    edges = []
    vertices = []
    for i in range(n):
        x, y = map(int, input().split())
        vertices.append((x, y))
    for i in range(n-1):
        (x1, y1) = vertices[i]
        for j in range(i+1, n):
            (x2, y2) = vertices[j] 
            d = round(math.sqrt((x1-x2)**2 + (y1-y2)**2), 2)
            edges.append((d, i, j))
    edges.sort()
    return edges, s, n

def find(parents, x):
    if x == parents[x]:
        return x
    return find(parents, parents[x])

def union(parents, x, y):
    a = find(parents, x)
    b = find(parents, y)
    parents[b] = a

def kruskal_modify(edges, parents, n, s):
    count_edges = 0
    for (d, u, v) in edges:
        if find(parents, u) != find(parents, v):
            union(parents, u, v)
            count_edges += 1
            if count_edges >= n - s:
                return '{:.2f}'.format(d)  

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        edges, s, n = read_input()
        parents = [i for i in range(n)]
        print(kruskal_modify(edges, parents, n, s))

