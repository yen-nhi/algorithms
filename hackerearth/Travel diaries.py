from collections import deque
import sys

def read_int():
    for line in sys.stdin:
        for num in line.split():
            yield int(num)

def bfs(matrix, n, m, nodes_of_2):
    q = deque(nodes_of_2)
    distances = [[0]*m for i in range(n)]
    res = 0
    while q:
        (x, y) = q.popleft()
        for (x2, y2) in ((x, y+1), (x, y-1), (x-1, y), (x+1, y)):
            if 0 <= x2 < n and 0 <= y2 < m and matrix[x2][y2] == 1:
                q.append((x2, y2))
                matrix[x2][y2] = 2
                distances[x2][y2] = distances[x][y] + 1
                res = max(res, distances[x2][y2])
    for i in range(n):
        for node in matrix[i]:
            if node == 1:
                return -1
    return res

gen = read_int()
n, m = next(gen), next(gen)
matrix = [[next(gen) for j in range(m)] for i in range(n)]
nodes_of_2 = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            nodes_of_2.append((i, j))
print(bfs(matrix, n, m, nodes_of_2))



