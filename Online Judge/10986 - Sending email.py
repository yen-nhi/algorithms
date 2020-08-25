#On Weighted Graph: Dijkstra’s, Easier

import heapq

def read_input():
    n, m, s, t = (int(i) for i in input().split())
    adjacent = [[] for i in range(n)]
    for i in range(m):
        u, v, w = (int(j) for j in input().split())
        adjacent[u].append((w, v))
        adjacent[v].append((w, u))
    return adjacent, s, t, n

def dijkstra(adjacent, s, t, n):
    prior_q = [(0, s)]
    heapq.heapify(prior_q)
    dist = [None] * n
    while prior_q:
        (d, u) = heapq.heappop(prior_q)
        if dist[u] == None:
            dist[u] = d
        if u == t:
            return dist[u]
        for (w, v) in adjacent[u]:
            if dist[v] == None:
                heapq.heappush(prior_q, (d+w, v))
    return 'unreachable'

if __name__ == "__main__":
    test = int(input())
    for num in range(test):
        adjacent, s, t, n = read_input()
        print('Case #' + str(num+1) + ':', dijkstra(adjacent, s, t, n))

