# coding = utf-8

import sys
input = sys.stdin.readline
from collections import deque

n, m, s = map(int, input().split())
shark = list()
for _ in range(s):
    shark.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
r = lambda x, y: 0<=x<n and 0<=y<m
visited = list(list(deque() for _ in range(m)) for _ in range(n))
# [idx, 크기]
for idx, sh in enumerate(shark):
    visited[sh[0]-1][sh[1]-1].append([idx, sh[4]])
res = 0
for j in range(m):
    for i in range(n):
        if len(visited[i][j]) == 1:
            res += visited[i][j][0][1]
            shark[visited[i][j][0][0]][4] = -1
            visited[i][j].pop()
            break
    er = set()
    for idx, sh in enumerate(shark):
        if sh[4] == -1:
            continue
        x, y = sh[0]-1, sh[1]-1
        visited[x][y].popleft()
        for _ in range(sh[2]):
            x, y = x+dx[sh[3]-1], y+dy[sh[3]-1]
            if r(x, y):
                continue
            if sh[3] == 1 or sh[3] == 3:
                sh[3] += 1
            else:
                sh[3] -= 1
            for _ in range(2):
                x, y = x+dx[sh[3]-1], y+dy[sh[3]-1]
        sh[0], sh[1] = x+1, y+1
        visited[sh[0]-1][sh[1]-1].append([idx, sh[4]])
        er.add((sh[0]-1, sh[1]-1))
    for ee in er:
        if len(visited[ee[0]][ee[1]]) < 2:
            continue
        visited[ee[0]][ee[1]] = deque(sorted(visited[ee[0]][ee[1]], key = lambda x:x[1]))
        while len(visited[ee[0]][ee[1]]) > 1:
            ii = visited[ee[0]][ee[1]].popleft()
            shark[ii[0]][4] = -1

print(res)