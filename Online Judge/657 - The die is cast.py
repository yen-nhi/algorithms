def dfs_dice_area(grid, x, y, visited, w, h):
    stack = [(x, y)]
    visited[x][y] = 'gray'
    dice = []
    while stack:
        (x, y) = stack.pop()
        dice.append((x, y))
        for (x1, y1) in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= x1 < h and 0 <= y1 < w and visited[x1][y1] == None and grid[x1][y1] in ('X', '*'):
                stack.append((x1, y1))
                visited[x1][y1] = 'gray'
    return dice

def dfs_dots(grid, dice, visited, x, y):
    stack = [(x, y)]
    visited[x][y] = 'black'
    while stack:
        (x, y) = stack.pop()
        for (x1, y1) in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if (x1, y1) in dice and visited[x1][y1] == 'gray' and grid[x1][y1] == 'X':
                stack.append((x1, y1))
                visited[x1][y1] = 'black'

def dice_cast(grid, visited, w, h):
    cast = []
    for x in range(h):
        for y in range(w):
            if visited[x][y] == None and grid[x][y] in ('X', '*'):
                dice = dfs_dice_area(grid, x, y, visited, w, h)
                count = 0
                for (i, j) in dice:
                    if grid[i][j] == 'X'and visited[i][j] == 'gray':
                        dfs_dots(grid, dice,  visited, i, j)
                        count += 1
                cast.append(count)
    cast.sort()
    return cast    
    
import sys
text = sys.stdin.readlines()
line = 0
counter = 1
while True:
    grid = []
    w, h = (int(i) for i in text[line].split())
    visited = [[None] * w for i in range(h)]
    if w == h == 0:
        break
    if w != 0 and h != 0:
        for i in range(h):
            grid.append(text[line+i+1].strip())
        cast = dice_cast(grid, visited, w, h)
        print('Throw', counter)
        print(*cast)
        print()
    line += h + 1
    counter += 1
    