import heapq

def shortest_path(slot, n, f):
    cost = [[float('inf'), i] for i in range(n)] 
    cost[0][0] = f
    prior_q = [(f, 0)]
    heapq.heapify(prior_q)
    while prior_q:
        d, u = heapq.heappop(prior_q)
        for (w, v) in slot[u]:
            if cost[v][0] > d + w:
                cost[v][0] = d + w
                heapq.heappush(prior_q, (cost[v][0], v))
    return cost

def parking_slot(cost, capacity):
    cost.sort()
    res = [-1] * k
    vehicles = 0
    for (c, i) in cost:
        for j in range(capacity[i]):
            res[vehicles] = c
            vehicles += 1
            if vehicles >= k:
                return res
    return res
   
n, m, f = map(int, input().split())
capacity = [int(i) for i in input().split()]
slot = [[] for i in range(n)]
for i in range(m):
    u, v, w = map(int, input().split())
    slot[u-1].append((w, v-1))
    slot[v-1].append((w, u-1))
k = int(input())

cost = shortest_path(slot, n, f)
print(cost)
print(*parking_slot(cost, capacity))