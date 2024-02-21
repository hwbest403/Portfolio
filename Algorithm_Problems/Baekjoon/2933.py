# coding = utf-8

import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int,input().split())
board = list(list(input().rstrip()) for _ in range(r))
n = int(input())
height = list(map(int, input().split()))
visited = list(list(-1 for _ in range(c)) for _ in range(r))
inrange = lambda x, y: 0 <= x < r and 0 <= y < c

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def printboard(board):
    for row in board:
        print(row)

def solprint(board):
    for row in board:
        for s in row:
            print(s, end="")
        print()

def erasemineral(h, f):
    if f:
        for i in range(c):
            if board[r-h][i] == 'x':
                board[r-h][i] = '.'
                break
    else:
        for i in range(c-1, -1, -1):
            if board[r-h][i] == 'x':
                board[r-h][i] = '.'
                break

def bfs(x, y, idx):
    need_visited = deque()
    v = list()
    need_visited.append((x, y))
    flag = True
    while need_visited:
        node = need_visited.popleft()
        tx, ty = node[0], node[1]
        if tx == len(board)-1:
            flag = False
        if visited[tx][ty] == -1:
            v.append((tx, ty))
            visited[tx][ty] = idx
            for d in range(4):
                nx, ny = tx + dx[d], ty + dy[d]
                if inrange(nx, ny) and board[nx][ny] == 'x':
                    need_visited.append((nx, ny))
    return flag, v

def findcluster(r, c):
    idx = 0
    need_down = list()
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'x' and visited[i][j] == -1:
                flag, tp = bfs(i, j, idx)
                if flag:
                    need_down.append(tp)
                idx += 1
    return need_down

def downcluster(need_down):
    for group in need_down:
        group.sort(key=lambda x:(x[1], x[0]), reverse=True)
        minv = len(board)+1
        for idx, node in enumerate(group):
            x, y = node[0], node[1]
            board[x][y] = '.'
            if idx != 0 and y == group[idx-1][1]:
                continue
            tp = 0
            for i in range(x+1, r):
                if board[i][y] == 'x':
                    break
                tp += 1
            if tp <= minv:
                minv = tp
        for node in group:
            board[node[0]+minv][node[1]] = 'x'

def freevisited(r, c):
    for i in range(r):
        for j in range(c):
            visited[i][j] = -1

def sol(r, c):
    flag = True
    for h in height:
        erasemineral(h, flag)
        need_down = findcluster(r, c)
        downcluster(need_down)
        freevisited(r, c)
        if flag:
            flag = False
        else:
            flag = True

sol(r, c)
solprint(board)