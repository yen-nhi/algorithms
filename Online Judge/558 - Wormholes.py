def read_input():
    n, m =  (int(i) for i in input().split())
    edges = []
    for i in range(m):
        u, v, w = (int(i) for i in input().split())
        edges.append((u, v, w))
    return edges, n

def bellman_ford(edges, n):
    dist = [float('inf')] * n
    dist[0] = 0
    for i in range(n-1):
        for (u, v, w) in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for (u, v, w) in edges:
            if dist[u] + w < dist[v]:
                return 'possible'
    return 'not possible'

if __name__ == "__main__":
    cases = int(input())
    for t in range(cases):
        edges, n = read_input()
        print(bellman_ford(edges, n))
    
        

