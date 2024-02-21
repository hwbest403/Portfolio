import sys
from collections import deque

input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
inrange = lambda x, y:0<=x<12 and 0<=y<6

def getdata():
    board = list(list(input().rstrip()) for _ in range(12))
    return board

def printboard(board):
    for row in board:
        print(row)

def down(tmp_break, board):
    col = set()
    for gp in tmp_break:
        for i, j in gp:
            board[i][j] = '.'
            col.add(j)
    for c in col:
        tmp_i = 11
        for i in range(11, -1, -1):
            if board[i][c] != '.':
                if tmp_i != i:
                    board[tmp_i][c] = board[i][c]
                    board[i][c] = '.'
                tmp_i -= 1
    return board

def bfs(board):
    need_visited, visited = deque(), list(list(False for _ in range(6)) for _ in range(12))
    need_break = list()
    for i in range(12):
        for j in range(6):
            if board[i][j] == '.':
                visited[i][j] = True
            else:
                gp = set()
                need_visited.append((i, j))
                while need_visited:
                    tx, ty = need_visited.popleft()
                    visited[tx][ty] = True
                    gp.add((tx, ty))
                    for d in range(4):
                        nx, ny = tx+dx[d], ty+dy[d]
                        if inrange(nx, ny) and not visited[nx][ny] and board[nx][ny] == board[tx][ty]:
                            need_visited.append((nx, ny))
                if len(gp) >= 4:
                    need_break.append(gp)
    return need_break

def sol():
    answer = 0
    board = getdata()
    while True:
        tmp_break = bfs(board)
        if not tmp_break:
            break
        else:
            answer += 1
            board = down(tmp_break, board)
    return answer

print(sol())