def dfs(adj, n, v):
    count_array = [1] * n
    order = []
    parents = [None] * n
    parents[v] = v
    stack = [v]
    while stack:
        v = stack.pop()
        order.append(v)
        for w in adj[v]:
            if parents[w] is None:
                stack.append(w)
                parents[w] = v
    while len(order) > 1:
        i = order.pop()
        count_array[parents[i]] += count_array[i]
    return count_array

n, q = map(int, input().split())
adj = [[] for i in range(n)]
edges = []
for i in range(n-1):
    u, v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)
    edges.append((u-1, v-1))
count_array = dfs(adj, n, 0)
for j in range(q):
    x = int(input())
    a, b = edges[x-1]
    k = min(count_array[a], count_array[b])
    print(k*(n-k))