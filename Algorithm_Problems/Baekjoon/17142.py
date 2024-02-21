# coding = utf-8

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
board = list(list(map(int,input().split())) for _ in range(n))
fish = 0
res = 0
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
inrange = lambda x, y: 0<=x<n and 0<=y<n

for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            continue
        if board[i][j] == 9:
            sx, sy = i, j
            s = [2, 0]
            board[i][j] = 0
            continue
        fish += 1

def bfs(x, y):
    need_visited = deque()
    visited = list(list(-1 for _ in range(n)) for _ in range(n))
    need_visited.append((x, y))
    minv = n**3
    minf = list()
    visited[x][y] = 0
    while need_visited:
        px, py = need_visited.popleft()
        for d in range(4):
            nx, ny = px+dx[d], py+dy[d]
            if inrange(nx, ny) and visited[nx][ny] == -1 and board[nx][ny] <= s[0]:
                if visited[px][py] + 1 > minv:
                    minf.sort(key=lambda x:(x[0], x[1]))
                    s[1] += 1
                    if s[0] == s[1]:
                        s[0] += 1
                        s[1] = 0
                    board[minf[0][0]][minf[0][1]] = 0
                    return minf[0][0], minf[0][1], minv
                if board[nx][ny] != 0 and board[nx][ny] < s[0]:
                    if minv == n**3:
                        minv = visited[px][py] + 1
                    minf.append((nx, ny))
                need_visited.append((nx, ny))
                visited[nx][ny] = visited[px][py] + 1
    if minf:
        minf.sort(key=lambda x: (x[0], x[1]))
        s[1] += 1
        if s[0] == s[1]:
            s[0] += 1
            s[1] = 0
        board[minf[0][0]][minf[0][1]] = 0
        return minf[0][0], minf[0][1], minv
    return -1, -1, -1

while fish > 0:
    sx, sy, t = bfs(sx, sy)
    if t == -1:
        break
    res += t
    fish -= 1

print(res)