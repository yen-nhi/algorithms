# Dijkstra’s

import math
import heapq

def cal_distance(x1, y1, x2, y2):
    d = round(math.sqrt((x2-x1)**2 + (y2-y1)**2), 2)
    return d

def read_input():
    dimension = input()
    if dimension == '*':
        return
    else:
        w, h = (int(i) for i in dimension.split())
    n = int(input())
    safe = [(0, 0)]
    for i in range(n):
        x, y = (float(j) for j in input().split())
        safe.append((x, y))
    safe.append((w, h))
    k = float(input())

    adjacent = [[] for i in range(n+2)]
    for u in range(n+2):
        for v in range(n+2):
            if safe[v] != safe[u]:
                (x1, y1), (x2, y2) = safe[u], safe[v]
                w = cal_distance(x1, y1, x2, y2)
                if w <= 1.5:
                    adjacent[u].append((w, v))
    
    return w, h, adjacent, k, n

def minfield(wid, hei, adjacent, k, n):
    prior_q = [(0,0)]
    heapq.heapify(prior_q)
    stepped = [None] * (n+2)
    while prior_q:
        d, u = heapq.heappop(prior_q)
        stepped[u] = d
        if d > k:
            return 'Boom!'
        for (w, v) in adjacent[u]:
            if v == n+1 and d+w <= k:
                return 'I am lucky!'
            if stepped[v] is None:
                heapq.heappush(prior_q, ((round(d+w, 2), v)))
    return 'Boom!'

if __name__ == "__main__":
    t = 0
    for wid, hei, adjacent, k, n in iter(read_input, None):
        print(minfield(wid, hei, adjacent, k, n))
        t += 1


                




            



    

