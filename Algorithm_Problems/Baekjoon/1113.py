# coding = utf-8

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
board = list(list(map(int,input().rstrip())) for _ in range(n))

def printboard(board):
    for row in board:
        print(row)

def bfs(x, y, h, visited):
    need_visitied = deque()
    need_visitied.append((x, y))
    visited[x][y] = True
    dx = (0, 0, -1, 1)
    dy = (-1, 1, 0, 0)
    cnt = 1
    flag = True
    while need_visitied:
        tx, ty = need_visitied.popleft()
        for d in range(4):
            nx, ny = tx+dx[d], ty+dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                flag = False
                continue
            if board[nx][ny] <= h and not visited[nx][ny]:
                visited[nx][ny] = True
                need_visitied.append((nx, ny))
                cnt += 1
    if flag:
        print(x, y, h, cnt)
        return cnt
    else:
        return 0

def sol():
    answer = 0
    for h in range(1, 10):
        visited = list(list(False for _ in range(m)) for _ in range(n))
        for i in range(n):
            for j in range(m):
                if board[i][j] <= h and not visited[i][j]:
                    answer += bfs(i, j, h, visited)
    print(answer)

sol()