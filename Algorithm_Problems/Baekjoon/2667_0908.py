import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = list(list(map(int, input().rstrip())) for _ in range(n))
need_visited = deque()
visited = list(list(False for _ in range(n)) for _ in range(n))
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
inrange = lambda x, y:0<=x<n and 0<=y<n

answer = 0
cnt_ls = list()
for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            visited[i][j] = True
        else:
            if not visited[i][j]:
                answer += 1
                gp = set()
                need_visited.append((i,j))
                while need_visited:
                    tx, ty = need_visited.popleft()
                    visited[tx][ty] = True
                    for d in range(4):
                        nx, ny = tx+dx[d], ty+dy[d]
                        if inrange(nx, ny) and not visited[nx][ny] and board[nx][ny] == 1:
                            need_visited.append((nx, ny))
                            gp.add((nx, ny))
                cnt_ls.append(len(gp)+1)

print(answer)
cnt_ls.sort()
for i in cnt_ls:
    print(i)