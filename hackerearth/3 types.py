def find(parents, x):
    while parents[x] != x:
        x = parents[x] 
    return x

def union(parents, x, y):
    parents[y] = find(parents, x)

def spanning_tree(edges, component, parents, ):
    for (u, v) in edges:
        x = find(parents, u)
        y = find(parents, v)
        if x != y:
            union(parents, x, y)
            component.add((u, v))
        
def detroy_roads(women_roads, men_roads, both_roads):
    parents = [i for i in range(n+1)]
    component = set()
    spanning_tree(both_roads, component, parents)
    for edges in (women_roads, men_roads):
        new_parents = parents.copy()
        spanning_tree(edges, component, new_parents)
    return len(component)

def result(weight, women_roads, men_roads, both_roads, m):
    for j in weight:
        if j < 3:
            return -1
    return m - detroy_roads(women_roads, men_roads, both_roads)

n, m = map(int, input().split())
women_roads = []
men_roads = []
both_roads = []
weight = [0] * n 
for i in range(m):
    u, v, type_ = map(int, input().split())
    if type_ == 3:
        both_roads.append((u, v))
        weight[u-1] += 3
        weight[v-1] += 3
    elif type_ == 2:
        women_roads.append((u, v))
        weight[u-1] += 2
        weight[v-1] += 2
    elif type_ == 1:
        men_roads.append((u, v))
        weight[u-1] += 1
        weight[v-1] += 1

print(result(weight, women_roads, men_roads, both_roads, m))