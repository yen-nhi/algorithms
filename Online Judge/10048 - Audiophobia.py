
import heapq

def read_input():
    n, m, q = (int(i) for i in input().split())
    if n == m == q == 0:
        return
    adjacent = [[] for i in range(n)]
    query = []
    for i in range(m):
        u, v, d = (int(i) for i in input().split())
        adjacent[u-1].append((d, v-1))
        adjacent[v-1].append((d, u-1))
    for j in range(q):
        a, b = (int(i) for i in input().split())
        query.append((a-1, b-1))
    return adjacent, query

def prim(adjacent, a, b):
    prior_q = [(0, a)]
    heapq.heapify(prior_q)
    max_d = 0
    n = len(adjacent)
    visited = [False] * n
    while prior_q:
        (d, u) = heapq.heappop(prior_q)
        visited[u] = True
        if d > max_d:
            max_d = d
        if u == b:
            return max_d
        for (w, v) in adjacent[u]:
            if not visited[v]:
                heapq.heappush(prior_q, (w, v))
    return "no path"

if __name__ == "__main__":
    i = 1
    for adjacent, query in iter(read_input, None):
        if i != 1:
            print()
        print("Case #"+ str(i))
        for (a, b) in query:
            print(prim(adjacent, a, b))
        i += 1
