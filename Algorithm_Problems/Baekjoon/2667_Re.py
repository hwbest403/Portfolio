# coding = utf-8

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
board = list(list(map(int,input().rstrip())) for _ in range(n))
visited = list(list(False for _ in range(n)) for _ in range(n))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(s):
    res = 0
    need_visited = deque()
    need_visited.append(s)
    while need_visited:
        node = need_visited.popleft()
        x, y = node[0], node[1]
        if not visited[x][y]:
            visited[x][y] = True
            res += 1
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<n and 0<=ny<n and board[nx][ny] == 1:
                    need_visited.append([nx,ny])
    return res

idx = 0
ans = list()
for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            visited[i][j] = True
        else:
            if not visited[i][j]:
                res = bfs([i, j])
                if res > 0:
                    ans.append(res)
                    idx += 1
ans.sort()
print(idx)
for n in ans:
    print(n)