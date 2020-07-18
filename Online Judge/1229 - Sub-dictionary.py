# Tajan's Algorithms

def dfs_tajan(id, low, on_stack, stack, forest, v, d):
    d += 1
    id[v], low[v] = d, d
    on_stack[v] = True
    stack.append(v)
    for u in adj[v]:
        if id[u] == 0:
            dfs_tajan(id, low, on_stack, stack, forest, u, d)
        if on_stack[u]:
            low[v] = min(low[u], low[v])
    if id[v] == low[v]:
        component = []
        while True:
            w = stack.pop()
            component.append(w)
            on_stack[w] = False
            if v == w:
                break
        forest.append(component)

def dfs(adj, v, visited, sub_dic):
    visited[v] = True
    sub_dic.append(v)
    for u in adj[v]:
        if not visited[u]:
            dfs(adj, u, visited, sub_dic)

def tajan(adj, n):
    low = [0] * n
    id = [0] * n
    stack = []
    on_stack = [False] * n
    forest = []
    for v in range(n):
        if id[v] == 0:
            dfs_tajan(id, low, on_stack, stack, forest, v, 0)
    scc = []
    for i in range(len(forest)):
        if len(forest[i]) > 1:
            scc += forest[i]
    visited = [False] * n
    sub_dic = []
    for w in scc:
        if not visited[w]:
            dfs(adj, w, visited, sub_dic)
    return sub_dic

def read_input():
    n = int(input())
    if n == 0:
        return
    index = 0
    dic = {}
    adj = [[] for i in range(n)]
    for i in range(n):
        seq = input().split()
        for word in seq:
            if word not in dic:
                dic[word] = index
                index += 1
            if word != seq[0]:
                adj[dic[seq[0]]].append(dic[word])
        adj[dic[seq[0]]] = list(set(adj[dic[seq[0]]]))
    dic = dict(map(reversed, dic.items()))
    return n, dic, adj 

if __name__ == "__main__":
    i = 1
    for n, dic, adj in iter(read_input, None):
        sub_dic =  tajan(adj, n)
        num_of_words = len(sub_dic)
        for j in range(len(sub_dic)):
            sub_dic[j] = dic[sub_dic[j]]
        sub_dic.sort()
        print(num_of_words)
        print(*sub_dic)
        i += 1
