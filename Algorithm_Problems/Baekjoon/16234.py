# coding = utf-8

import sys
input = sys.stdin.readline
from collections import deque

n, l, r = map(int,input().split())
A = list(list(map(int,input().split())) for _ in range(n))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs() :
    visited = list(list(False for _ in range(n)) for _ in range(n))
    union = list()
    flag = False
    for i in range(n) :
        for j in range(n) :
            if visited[i][j]:
                continue
            else :
                t = 0
                union.append(list())
                need_visited = deque()
                need_visited.append((i,j))
                while need_visited :
                    node = need_visited.popleft()
                    x, y = node[0], node[1]
                    if not visited[x][y]:
                        visited[x][y] = True
                        union[-1].append((x,y))
                        t += A[x][y]
                        for d in range(4) :
                            nx, ny = x+dx[d], y+dy[d]
                            if 0<=nx<n and 0<=ny<n and l<=abs(A[nx][ny]-A[x][y])<=r :
                                need_visited.append((nx,ny))
                for node in union[-1]:
                    A[node[0]][node[1]] = t//len(union[-1])
                if len(union[-1]) >= 2:
                    flag = True
    return flag

res = 0
while True :
    if not bfs():
        break
    res += 1
print(res)