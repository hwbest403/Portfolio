# coding = utf-8

import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int,input().split())
board = list(list(input().rstrip()) for _ in range(n))
visited = list(list(list(list(False for _ in range(m)) for _ in range(n)) for _ in range(m)) for _ in range(n))

for i in range(n) :
    for j in range(m) :
        if board[i][j] == 'R' :
            rx, ry = i, j
        if board[i][j] == 'B' :
            bx, by = i, j
visited[rx][ry][bx][by] = True

def move(x, y, dir) :
    nx, ny = x, y
    m = 0
    while True :
        nx, ny = nx+dx[dir], ny+dy[dir]
        m += 1
        if board[nx][ny] == '#' :
            nx, ny = nx-dx[dir], ny-dy[dir]
            m -= 1
            return nx, ny, m
        if board[nx][ny] == 'O' :
            return nx, ny, m

def bfs(rx,ry,bx,by) :
    need_visited = deque()
    need_visited.append((rx,ry,bx,by,0))
    while need_visited :
        # print(need_visited)
        nrx, nry, nbx, nby, flag = need_visited.popleft()
        if flag >= 10 :
            break
        for i in range(4) :
            nxrx, nxry, rm = move(nrx, nry, i)
            nxbx, nxby, bm = move(nbx, nby, i)
            # print(i, nxrx, nxry, nxbx, nxby)
            if board[nxbx][nxby] == 'O' :
                continue
            if board[nxrx][nxry] == 'O' :
                print(flag + 1)
                return
            if nxrx == nxbx and nxry == nxby :
                if rm > bm :
                    nxrx, nxry = nxrx-dx[i], nxry-dy[i]
                else :
                    nxbx, nxby = nxbx-dx[i], nxby - dy[i]
            if visited[nxrx][nxry][nxbx][nxby] == False :
                visited[nxrx][nxry][nxbx][nxby] = True
                need_visited.append((nxrx, nxry, nxbx, nxby, flag+1))
    print(-1)
    return

bfs(rx, ry, bx, by)