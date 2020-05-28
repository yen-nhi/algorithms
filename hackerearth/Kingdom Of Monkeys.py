def dfs(adj, v, weights):
    value = weights[v]
    stack = [v]
    weights[v] = -1
    while stack:
        v = stack.pop()
        for w in adj[v]:
            if weights[w] != -1:
                stack.append(w)
                value += weights[w]
                weights[w] = -1
    return value

def max_prize(adj, n, weights):
    max_prize = 0
    for v in range(n):
        if weights[v] != -1:
            max_prize = max(max_prize, dfs(adj, v, weights))
    return max_prize

for t in range(int(input())):
    n, m = map(int, input().split())
    adj = [[] for i in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    weights = [int(i) for i in input().split()]
    print(max_prize(adj, n, weights))