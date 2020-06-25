def dfs(adjacent_list, reversed_adj, n):
    order = []
    visited = [False] * n
    for v in range(n):
        if not visited[v]:
            stack = [v]
            visited[v] = True
            while stack:
                u = stack[-1]
                for v in adjacent_list[u]:
                    if not visited[v]:
                        stack.append(v)
                        visited[v] = True
                if stack[-1] == u:
                    order.append(stack.pop())
    scc = []
    visited = [False] * n
    while order:
        v = order.pop()
        if not visited[v]:
            stack = [v]
            visited[v] = True
            component = [v]
            while stack:
                u = stack.pop()
                for v in reversed_adj[u]:
                    if not visited[v]:
                        stack.append(v)
                        component.append(v)
                        visited[v] = True
            scc.append(component)
    return scc

import sys
text = sys.stdin.readlines()
line = 0
test = 1
while line < len(text):
    n, m = map(int, text[line].split())
    directory = {}
    adjacent_list = [[] for i in range(n)]
    reversed_adj = [[] for i in range(n)]
    num = 0
    for i in range(m):
        name1, name2 = text[line+i+1].split()
        for name in (name1, name2):
            if name not in directory:
                directory[name] = num
                num += 1
        adjacent_list[directory[name1]].append(directory[name2])
        reversed_adj[directory[name2]].append(directory[name1])
    line += m + 1
    directory = {value:key for (key, value) in directory.items()}
    if n != 0:
        print('Calling circles for data set', str(test)+':')
        if m != 0:
            for component in dfs(adjacent_list, reversed_adj, n):
                component.sort()
                res = [directory[i] for i in component]
                print(', '.join(res))
        print()
    test += 1