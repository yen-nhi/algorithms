
import heapq 

def read_input():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u-1, v-1))
    edges.sort()
    return edges, n

def find(parents, x):
    if parents[x] == x:
        return x
    return(find(parents, parents[x]))

def union(parents, x, y):
    a = find(parents, x)
    b = find(parents, y)
    parents[b] = a

def kruskal(edges, n, i, j):
    parents = [i for i in range(n)]
    mst_1 = []
    cost = 0
    for (w, u, v) in edges:
        if (u, v) != (i, j) and find(parents, u) != find(parents, v):
            union(parents, u, v)
            mst_1.append((w, u, v))
            cost += w
    return cost, mst_1

def sec_mst(edges, mst_1, n):
    cost_mst2 = float('inf')
    for (w2, u2, v2) in mst_1:
        cost, mst_2 = kruskal(edges, n, u2, v2)
        if len(mst_2) == n-1 and cost < cost_mst2:
            cost_mst2 = cost
    return cost_mst2     

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        edges, n = read_input()
        cost_mst1, mst_1 = kruskal(edges, n, -1, -1)
        cost_mst2 = sec_mst(edges, mst_1, n)
        if cost_mst2 > cost_mst1:
            print(cost_mst1, cost_mst2)
        else:
            print(cost_mst1, cost_mst1)
