def dfs(grid, x, y):
    count = 1
    row, col = len(grid), len(grid[0]) - 1
    visited = [[False] * col for i in range(row)]
    visited[x][y] = True
    stack = [(x, y)]
    while stack:
        (x, y) = stack.pop()
        for (x1, y1) in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= x1 < row and 0 <= y1 < col and not visited[x1][y1] and grid[x1][y1] == '0':
                stack.append((x1, y1))
                count += 1
                visited[x1][y1] = True
    return count

import sys
input_ = sys.stdin.readlines()
line = 1
n = len(input_)
for t in range(int(input_[0])):
    x, y = (int(i)-1 for i in input_[line+1].split())
    grid = []
    line += 2
    while line < n and input_[line] != "\n":
        if line == n -1:
            input_[line] += 'n'
        grid.append(input_[line])
        line += 1
    print(dfs(grid, x, y))
    print()
    