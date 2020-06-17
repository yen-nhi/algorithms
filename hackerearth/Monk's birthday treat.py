def dfs(adjacent, v):
    stack = [v]
    visited = [False] * n
    count = 0
    while stack:
        u = stack.pop() 
        for v in adjacent[u]:
            if not visited[v]:
                stack.append(v)
                visited[v] = True
                count += 1
    return count

def birthday_invite(adjacent, n):
    min_invite = n
    for v in range(n):
        w = dfs(adjacent, v)
        min_invite = min(min_invite, w)
    if min_invite < 1:
        min_invite = 1
    return min_invite

n, m = map(int, input().split())
adjacent = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    adjacent[u-1].append(v-1)
print(birthday_invite(adjacent, n))