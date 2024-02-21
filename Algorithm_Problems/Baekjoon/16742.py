# coding = utf-8

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
board = list(list(input().rstrip()) for _ in range(n))
visited = list(list(-1 for _ in range(m)) for _ in range(n))

dir = {'U':0, 'D':1, 'L':2, 'R':3}
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
group = 0

def dfs(i, j) :
    need_visited, path = deque(), list()
    need_visited.append([i, j])
    while need_visited :
        node = need_visited.popleft()
        x, y = node[0], node[1]
        if visited[x][y] != -1 :
            if visited[x][y] != group :
                for p in path :
                    visited[p[0]][p[1]] = visited[x][y]
                return 1
        if visited[x][y] == -1:
            visited[x][y] = group
            path.append([x, y])
            nx, ny = x+dx[dir[board[x][y]]], y+dy[dir[board[x][y]]]
            need_visited.append([nx, ny])
    return 0

for i in range(n) :
    for j in range(m) :
        if visited[i][j] == -1 :
            flag = dfs(i, j)
            if flag == 0 :
                group += 1
print(group)