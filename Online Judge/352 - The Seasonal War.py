
def dfs(matrix, x, y, visited):
    adjacent = ((0, 1), (0,-1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1,-1), (-1, 1))
    visited[x][y] = True
    stack = [(x, y)]
    while stack:
        (x, y) = stack.pop()
        for (x1, y1) in adjacent:
            x2, y2 = x + x1, y + y1
            if 0 <= x2 < n and 0 <= y2 < n and matrix[x2][y2] == '1' and not visited[x2][y2]:
                stack.append((x2, y2))
                visited[x2][y2] = True

def count_eagle(matrix, n):
    visited = [[False]*n for i in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == '1' and not visited[i][j]:
                dfs(matrix, i, j, visited)
                count += 1
    return count

import sys
text = sys.stdin.readlines()
i = 0
count = 0
while i < len(text):
    n = int(text[i])
    matrix = text[i+1:i+n+1]
    i += n+1
    count += 1
    res = count_eagle(matrix, n)
    print('Image number', count, 'contains', res, 'war eagles.')