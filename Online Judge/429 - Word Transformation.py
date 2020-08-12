from collections import deque
import sys

def read_input(text, line):
    adjacent = dict()
    dic = [[] for i in range(10)]
    i = line
    while True:
        string = text[i].strip()
        i += 1
        if string == '*':
            break
        p = len(string)
        adjacent[string] = []
        for word in dic[p-1]:
            different = 0
            for j in range(p):
                if word[j] != string[j]:
                    different += 1
                    if different > 1: 
                        break
            if different == 1:
                adjacent[string].append(word)
                adjacent[word].append(string)
        dic[p-1].append(string)
    query = []
    while text[i] != '\n':
        query.append((text[i].strip().split()))
        i += 1
        if i >= len(text):
            break
    return adjacent, query, i

def bfs(adjacent, u, w):
    q = deque([u])
    visited = {}
    for key in adjacent:
        visited[key] = -1
    visited[u] = 0
    while q:
        u = q.popleft()
        if u == w:
            return visited[u]
        for v in adjacent[u]:
            if visited[v] == -1:
                q.append(v)
                visited[v] = visited[u] + 1

if __name__ == "__main__":
    text = sys.stdin.readlines()
    line = 2
    for j in range(int(text[0])):
        if 0 < j < len(text):
            print()   
        adjacent, query, i = read_input(text, line)
        line = i
        for (u, w) in query:
            print(u, w, bfs(adjacent, u, w))
        
