
import heapq

def read_input():
    n = int(input())
    exit_ = int(input()) - 1
    timer = int(input())
    m = int(input())
    adjacent = [[] for i in range(n)]
    for i in range(m):
        u, v, w = map(int, input().split())
        adjacent[v-1].append((w, u-1))
    return adjacent, n, m, exit_, timer

def dijsktra(adjacent, n, exit_):
    prior_q = [(0, exit_)]
    heapq.heapify(prior_q)
    dist = [float('inf')] * n
    while prior_q:
        d, u = heapq.heappop(prior_q)
        if d < dist[u]:
            dist[u] = d
        for (w, v) in adjacent[u]:
            if dist[v] == float('inf'):
                heapq.heappush(prior_q, (d+w, v))
    return dist

if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        input()
        adjacent, n, m, exit_, timer = read_input()
        dist = dijsktra(adjacent, n, exit_)
        count = 0
        for d in dist:
            if d <= timer:
                count += 1
        print(count)
        if t < test_cases - 1:
            print()
        



