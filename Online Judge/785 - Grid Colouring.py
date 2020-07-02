
def dfs(grid, x, y, mark, m):
    stack = [(x, y)]
    grid[x][y] = mark
    while stack:
        (x, y) = stack.pop()
        for (x1, y1) in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= x1 < m and 0 <= y1 < len(grid[x1]) and grid[x1][y1] == ' ':
                stack.append((x1, y1))
                grid[x1][y1] = mark


def filling(grid, m):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            char = ['X', ' ', '_']
            if grid[row][col] not in char:
                x, y = row, col
                mark = grid[x][y]
                char.append(mark)
                dfs(grid, x, y, mark, m)
    
import sys
input_ = sys.stdin.readlines()
line = 0
while True:
    grid = []
    while input_[line][0] != '_':
        grid.append([i for i in input_[line][:len(input_[line])-1]])
        line += 1
    line += 2
    m = len(grid)
    filling(grid, m)
    for row in grid:
        print(''.join(row))
    print('_____________________________')
    if line >= len(input_) - 1:
        break
    print()

