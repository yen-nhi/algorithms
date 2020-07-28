
def read_input():
    n, m = map(int, input().split())
    if n == m == 0:
        return
    edges = []
    parents = []
    dic = {}
    for i in range(n):
        station = input()
        parents.append(i)
        dic[station] = i
    for j in range(m):
        u, v, w = input().split()
        w = int(w)
        edges.append((w, dic[u], dic[v]))
    edges.sort()
    start = input()
    return edges, parents, n

def find(parents, x):
    if x == parents[x]:
        return x
    return find(parents, parents[x])

def union(parents, x, y):
    a = find(parents, x)
    b = find(parents, y)
    parents[b] = a

def kruskal(edges, n, parents):
    min_cost = 0
    count_edges = n-1
    for (w, u, v) in edges:
        if find(parents, u) != find(parents, v):
            union(parents, u, v)
            min_cost += w
            count_edges -= 1
    if count_edges > 0:
        return 'Impossible'
    return min_cost

if __name__ == "__main__":
    i = 0
    for edges, parents, n in iter(read_input, None):
        print(kruskal(edges, n, parents))
        i += 1

