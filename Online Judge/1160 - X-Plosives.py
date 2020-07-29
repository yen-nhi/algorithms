
import sys

def find(parents, x):
    if x == parents[x]:
        return x
    return find(parents, parents[x])

def union(parents, x, y):
    a = find(parents, x)
    b = find(parents, y)
    parents[b] = a

def kruskal_simple(edges):
    counter = 0
    for (u, v) in edges:
        if find(parents, u) == find(parents, v):
            counter += 1
        else:
            union(parents, u, v)
    return counter

if __name__ == "__main__":
    input_ = sys.stdin.readlines()
    line = 0
    m = len(input_)
    while line < m:
        edges = []
        parents = [i for i in range(100001)]
        while input_[line].strip() != '-1':
            u, v = map(int, input_[line].split())
            line += 1
            edges.append((u, v))
            parents[u] = u
            parents[v] = v
        line += 2
        print(kruskal_simple(edges))
