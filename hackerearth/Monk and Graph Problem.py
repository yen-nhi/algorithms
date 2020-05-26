# Depth-first search

def dfs(adj, v, visited, count):
    visited[v] = True
    for w in adj[v]:
        count += 1
        if not visited[w]:
            count = dfs(adj, w, visited, count)
    return count

def max_edges(adj, n):
    max_edges = 0
    visited = [False] * n
    for v in range(n):
        if not visited[v]:
            max_edges = max(max_edges, dfs(adj, v, visited, 0)//2)
    return max_edges


n, m = map(int, input().split())
adj = [[] for i in range(n)]
edges = []
visited = [False] * n
for i in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)
print(max_edges(adj, n))