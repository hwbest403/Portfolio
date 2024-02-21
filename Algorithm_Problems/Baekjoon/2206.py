# coding = utf-8
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
board = list(list(map(int,input().rstrip())) for _ in range(n))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

inrange = lambda x, y: 0 <= x < n and 0 <= y < m

def bfs():
    visited = list(list(False for _ in range(m)) for _ in range(n))
    need_visited = deque()
    need_visited.append((0, 0, 1, flag))
    while need_visited:
        x, y, distance = need_visited.popleft()
        if not visited[x][y]:
            visited[x][y] = True
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if nx == n-1 and ny == m-1:
                    return distance+1
                if inrange(nx, ny) and board[nx][ny] == 0:
                    need_visited.append((nx, ny, distance+1))
    return -1

def backtracking():
    min_val = n*m+1
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                board[i][j] = 0
                tmp = bfs()
                board[i][j] = 1
                if tmp == -1:
                    continue
                if tmp < min_val:
                    min_val = tmp
    if min_val == n*m+1:
        return -1
    else:
        return min_val

print(backtracking())
