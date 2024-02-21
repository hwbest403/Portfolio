# coding = utf-8

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
board = list(list(input().rstrip()) for _ in range(n))
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
inrange = lambda x, y: 0<=x<n and 0<=y<n

flag = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == '#' and flag == 0:
            sx, sy = i, j
            flag = 1
        elif board[i][j] == '#' and flag == 1:
            ex, ey = i, j

def sol(sx, sy, ex, ey):
    need_visited, visited = deque(), list(list(list(-1 for _ in range(4)) for _ in range(n)) for _ in range(n))
    for d in range(4):
        need_visited.append((sx, sy, d))
    while need_visited:
        node = need_visited.popleft()
        x, y, d = node[0], node[1], node[2]
        if x == ex and y == ey:
            print(visited[x][y][d]+1)
            return
        nx, ny = x + dx[d], y + dy[d]
        if inrange(nx, ny):
            if board[nx][ny] != '*':
                if visited[nx][ny][d] == -1 or visited[nx][ny][d] > visited[x][y][d]:
                    visited[nx][ny][d] = visited[x][y][d]
                    need_visited.appendleft((nx, ny, d))
                if board[nx][ny] == '!':
                    if d<2:
                        for nd in range(2, 4):
                            if visited[nx][ny][nd] == -1 or visited[nx][ny][nd] > visited[x][y][d] + 1:
                                visited[nx][ny][nd] = visited[x][y][d] + 1
                                need_visited.append((nx, ny, nd))
                    else:
                        for nd in range(2):
                            if visited[nx][ny][nd] == -1 or visited[nx][ny][nd] > visited[x][y][d] + 1:
                                visited[nx][ny][nd] = visited[x][y][d] + 1
                                need_visited.append((nx, ny, nd))

sol(sx, sy, ex, ey)