
import heapq

def read_input():
    m = int(input())
    adjacent = dict()
    for i in range(m):
        a, b, dep, dur = input().split()
        if int(dep) < 18:
            dep = int(dep) + 6
        else:
            dep = int(dep) + 6 - 24
        for city in (a, b):
            if city not in adjacent:
                adjacent[city] = []
        adjacent[a].append((dep, int(dur), b))
    s, t = input().split()
    return adjacent, s, t

def dijsktra(adjacent, s, t):
    if s == t:
        return [0,0]
    prior_q = [(0, 0, s)]
    heapq.heapify(prior_q)
    dist = dict()
    for city in adjacent:
        dist[city] = [float('inf'), 0]
    dist[s] = (0, 0)
    while prior_q:
        d, ar, u = heapq.heappop(prior_q)
        if u not in adjacent:
            return 
        if d < dist[u][0]:
            dist[u] = [d, ar]
        for (dep_v, dur_v, v) in adjacent[u]:
            if 0 <= dep_v < 12 and dep_v + dur_v <= 12:
                if dist[v][0] == float('inf'):
                    if u == s:
                        time = dur_v
                    else:
                        if dist[u][1] <= dep_v:
                            time = dist[u][0] + (dep_v - dist[u][1]) + dur_v
                        else:
                            time = dist[u][0] + (dep_v + 24 - dist[u][1]) + dur_v
                    arrive_v = dep_v + dur_v
                    heapq.heappush(prior_q, (time, arrive_v, v))
    if t in adjacent:
        return dist[t]
    else:
        return

if __name__ == "__main__":
    test = int(input())
    for case in range(test):
        adjacent, s, t = read_input()
        res = dijsktra(adjacent, s, t)
        print('Test Case', str(case+1) + '.')
        if res is None or res[0] == float('inf'):
            print('There is no route Vladimir can take.')
        else:
            if res[1] >= res[0]%24:
                print('Vladimir needs', res[0]//24, 'litre(s) of blood.')
            else:
                print('Vladimir needs', res[0]//24 + 1, 'litre(s) of blood.')
            