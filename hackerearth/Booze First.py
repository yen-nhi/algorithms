# Dijkstra's algorithm

import heapq

def shortest_paths(n, points, shops):
    distance = [float('inf')] * (n)
    prior_q = []
    heapq.heapify(prior_q)
    for s in shops:
        heapq.heappush(prior_q, (0, s))
        distance[s] = 0
    while prior_q:
        (d, u) = heapq.heappop(prior_q)
        if d < distance[u]:
            distance[u] = d
        for (w, v) in points[u]:
            if distance[v] > d + w:
                heapq.heappush(prior_q, (d+w, v))
    return distance

n, m = map(int, input().split())
points = [[] for i in range(n)]
for i in range(m):
    u, v, w = map(int, input().split())
    points[u-1].append([w, v-1])
    points[v-1].append([w, u-1])
b = int(input())
shops = [int(i) - 1 for i in input().split()]

array = shortest_paths(n, points, shops)
print(*array, sep= "\n")