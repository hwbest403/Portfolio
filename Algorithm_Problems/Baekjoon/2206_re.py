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
    True_visited = list(list(False for _ in range(m)) for _ in range(n))
    False_visited = list(list(False for _ in range(m)) for _ in range(n))
    need_visited = deque()
    if n == 1 and m == 1:
        return 1
    # x, y, distance, wall_flag
    need_visited.append((0, 0, 1, False))
    False_visited[0][0] = True
    while need_visited:
        x, y, distance, flag = need_visited.popleft()
        # print(x, y, distance, flag)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx == n-1 and ny == m-1:
                return distance+1
            if inrange(nx, ny):
                if not flag:
                    if board[nx][ny] == 0 and not False_visited[nx][ny]:
                        False_visited[nx][ny] = True
                        need_visited.append((nx, ny, distance+1, False))
                    if board[nx][ny] == 1 and not True_visited[nx][ny]:
                        True_visited[nx][ny] = True
                        need_visited.append((nx, ny, distance+1, True))
                else:
                    if board[nx][ny] == 0 and not True_visited[nx][ny]:
                        True_visited[nx][ny] = True
                        need_visited.append((nx, ny, distance+1, True))
    return -1

print(bfs())