from collections import deque
import sys

def bfs(adjacent, v, d):
    q = deque([v])
    level = {}
    for key in adjacent:
        level[key] = -1
    level[v] = 0
    while q:
        u = q.popleft()
        if u == '*':
            return d * 0.95**(level[u])
        for v in adjacent[u]:
            if level[v] == -1:
                q.append(v)
                level[v] = level[u] + 1
    return 0

def most_export(adjacent, export_value):
    max_value = -1
    max_planet = None
    for (d, v) in export_value:
        value = bfs(adjacent, v, d)
        if value > max_value:
            max_value = value
            max_planet = v
        if value == max_value:
            max_planet = min(max_planet, v)
    return max_planet

if __name__ == "__main__":
    input_ = sys.stdin.readlines()
    line = 0
    while line < len(input_):
        n = int(input_[line])
        adjacent = {}
        export_value = []
        for i in range(n):
            v, d, string = input_[line + 1 + i].strip().split()
            d = float(d)
            if v not in adjacent:
                adjacent[v] = []
            export_value.append((d, v))
            for letter in string:
                adjacent[v].append(letter)
                if letter not in adjacent:
                    adjacent[letter] = [v]
                else:
                    adjacent[letter].append(v)
        print('Import from', most_export(adjacent, export_value))
        line += n+1
    
        


