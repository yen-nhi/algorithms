from collections import deque

def read_input():
    n, m = (int(i) for i in input().split())
    if n == m == 0:
        return
    b = int(input())
    grid = [[-1 for j in range(m)] for i in range(n)]
    for i in range(b):
        input_ = [int(x) for x in input().split()]
        for j in input_[2:]:
            grid[input_[0]][j] = 1
    x1, y1 = (int(i) for i in input().split())
    x2, y2 = (int(i) for i in input().split())
    return grid, x1, y1, x2, y2, n, m

def bfs(grid, x1, y1, x2, y2, n, m):
    q = deque([(x1, y1)])
    grid[x1][y1] = 0
    while q:
        xu, yu = q.popleft()
        if xu == x2 and yu == y2:
            return grid[xu][yu]
        for (xv, yv) in ((xu-1, yu), (xu+1, yu), (xu, yu+1), (xu, yu-1)):
            if 0 <= xv < n and 0 <= yv < m and grid[xv][yv] == -1:
                q.append((xv, yv))
                grid[xv][yv] = grid[xu][yu] + 1
        
if __name__ == "__main__":
    t = 1
    for grid, x1, y1, x2, y2, n, m in iter(read_input, None):
        print(bfs(grid, x1, y1, x2, y2, n, m))
        t += 1

