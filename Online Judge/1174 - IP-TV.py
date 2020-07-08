# Prim's algorithm

import random 
import heapq

def prim(adjacent):
    visited = {}
    for vertex in adjacent.keys():
        visited[vertex] = False
    v = random.choice(list(adjacent))
    prior_queue = [(0, v)]
    visited[v] = True
    heapq.heapify(prior_queue)
    cost = 0
    while prior_queue:
        (c, u) = heapq.heappop(prior_queue)
        if not visited[u]:
            visited[u] = True
            cost += c
        for (w, v) in adjacent[u]:
            if not visited[v]:
                heapq.heappush(prior_queue, (w, v))
    return cost
    
test = int(input())
for t in range(test):
    blank = input()
    adjacent = {}
    n = int(input())
    m = int(input())
    if t > 0:
        print()
    for i in range(m):
        city_1, city_2, cost = input().split()
        cost = int(cost)
        if city_1 not in adjacent:
            adjacent[city_1] = [(cost, city_2)]
        else:
            adjacent[city_1].append((cost, city_2))
        if city_2 not in adjacent:
            adjacent[city_2] = [(cost, city_1)]
        else:
            adjacent[city_2].append((cost, city_1))
    print(prim(adjacent))
        
