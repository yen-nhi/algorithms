def dfs(board, x, y, visited):
    stack = [(x, y)]
    visited[x][y] = True
    color = None
    count = 0
    while stack:
        (x, y) = stack.pop()
        count += 1
        for (x1, y1) in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= x1 < 9 and 0 <= y1 < 9 and not visited[x1][y1]:
                if board[x1][y1] == ".":
                    stack.append((x1, y1))
                    visited[x1][y1] = True
                elif board[x1][y1] == "X" and color is None:
                    color = 'black'
                elif board[x1][y1] == "X" and color == "white":
                    color = 'gray'
                elif board[x1][y1] == "O" and color is None:
                    color = 'white'
                elif board[x1][y1] == "O" and color == "black":
                    color = 'gray'
    return count, color    

def count_stones(board):
    black = 0
    white = 0
    visited = [[False] * 9 for i in range(9)]
    for i in range(9):
        for j in range(9):
            if not visited[i][j] and board[i][j] == ".":
                count, color = dfs(board, i, j, visited)
                if color == 'black':
                    black += count
                elif color == 'white':
                    white += count
            elif board[i][j] == "X":
                black += 1
            elif board[i][j] == "O":
                white += 1
    return black, white

import sys
text = sys.stdin.readlines()
n = int(text[0])
i = 1
while i < len(text):
    board = []
    for j in range(9):
        board.append(text[i+j].strip())
    i += 9
    b, w = count_stones(board)
    print("Black", b, "White", w)