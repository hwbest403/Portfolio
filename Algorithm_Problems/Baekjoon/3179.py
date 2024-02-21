import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int,input().split())
board = list(list(input().rstrip()) for _ in range(r))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
root = list(list((i, j) for j in range(c)) for i in range(r))
rank = list(list(0 for _ in range(c)) for _ in range(r))
visited = list(list(False for _ in range(c)) for _ in range(r))
swan = list()
melt_point = deque()

for i in range(r):
    for j in range(c):
        if board[i][j] == 'L':
            swan.append((i, j))
            board[i][j] = '.'
        if board[i][j] == '.' and not visited[i][j]:
            visited[i][j] = True
            for d in range(4):
                nx, ny = i+dx[d], j+dy[d]
                if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and (board[nx][ny] == '.' or board[nx][ny] == 'L'):
                    root[nx][ny] = (i, j)
                elif 0<=nx<r and 0<=ny<c and not visited[nx][ny] and board[nx][ny] == 'X':
                    board[nx][ny] = '.'
                    visited[nx][ny] = True
                    melt_point.append((nx, ny))

def find(v: tuple) -> tuple:
    if v != root[v[0]][v[1]]:
        root[v[0]][v[1]] = find(root[v[0]][v[1]])
    return root[v[0]][v[1]]

def union(v1: tuple, v2: tuple):
    p1 = root[v1[0]][v1[1]]
    p2 = root[v2[0]][v2[1]]
    if rank[p1[0]][p1[1]] > rank[p2[0]][p2[1]]:
        root[p2[0]][p2[1]] = p1
    elif rank[p1[0]][p1[1]] < rank[p2[0]][p2[1]]:
        root[p1[0]][p1[1]] = p2
    else:
        root[p2[0]][p2[1]] = p1
        rank[p1[0]][p1[1]] += 1

def icebreak(melt_point: deque) -> deque:
    tmp = deque()
    while melt_point:
        x, y = melt_point.popleft()
        board[x][y] = '.'
        union_point = list()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and board[nx][ny] == 'X':
                visited[nx][ny] = True
                tmp.append((nx, ny))
            elif 0<=nx<r and 0<=ny<c and board[nx][ny] == '.':
                union_point.append((nx, ny))
        for ut in union_point:
            if find(ut) != find((x, y)):
                union(ut, (x, y))
    return tmp

def sol(melt_point: deque) -> int:
    day = 0
    while find(swan[0]) != find(swan[1]):
        melt_point = icebreak(melt_point)
        day += 1
    return day

print(sol(melt_point))