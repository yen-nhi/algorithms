#  Depth-first search

def finding_exit(matrix, i, j, n, count, visited):
    print(i,j)
    if i == n-1 and j == n-1:
        count += 1
        print('cccccccccccc=', count)
        return count
    if matrix[0][0] == 1 and matrix[n-1][n-1] == 0:
        matrix[0][0] = 0  
    if 0 <= i <n and 0 <= j < n and not visited[i][j] and matrix[i][j] == 0:
        visited[i][j] = True
        for (x, y) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            count = finding_exit(matrix, i+x, j+y, n, count, visited)
        visited[i][j] = False
    return count

for t in range(int(input())):
    n = int(input())
    visited = [[False] * n for i in range(n)]
    matrix = []
    for i in range(n):
        matrix.append([int(j) for j in input().split()])
    print(finding_exit(matrix, 0, 0, n, 0, visited))