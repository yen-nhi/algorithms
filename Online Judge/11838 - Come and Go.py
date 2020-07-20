# Tajan's algorithm

def read_input():
    n, m = map(int, input().split())
    if n == m == 0:
        return
    adjacent = [[] for i in range(n)]
    for i in range(m):
        u, v, p = map(int, input().split())
        adjacent[u-1].append(v-1)
        if p == 2:
            adjacent[v-1].append(u-1)
    return adjacent, n

def dfs_tajan(ide, low, stack, onstack, v, d):
    d += 1
    ide[v], low[v] = d, d
    onstack[v] = True
    stack.append(v)
    for u in adjacent[v]:
        if ide[u] == 0:
            dfs_tajan(ide, low, stack, onstack, u, d)
        if onstack[u]:
            low[v] = min(low[u], low[v])
    if low[v] == ide[v]:
        count = 0
        while True:
            w = stack.pop()
            onstack[w] = False
            count += 1
            if w == v:
                break
        if count == n:
            return True
        return False

if __name__ == "__main__":
    i = 0
    for adjacent, n in iter(read_input, None):
        ide, low, onstack, stack = [0]*n, [0]*n, [False]*n, []
        boo = dfs_tajan(ide, low, stack, onstack, 0, 0)
        if boo:
            print(1)
        else:
            print(0)



