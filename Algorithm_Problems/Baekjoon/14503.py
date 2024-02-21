# coding = utf-8

import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
r, c, d = list(map(int,input().split()))
board = list(list(map(int,input().split())) for _ in range(n))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

res = 0

def robot(r, c, d):
    global res

    # 1 step
    if board[r][c] == 0 :
        board[r][c] = 2
        res += 1

    flag = 0
    for _ in range(4):
        d -= 1
        d %= 4
        nx, ny = r+dx[d], c+dy[d]
        # 3 step
        if board[nx][ny] == 0:
            robot(nx, ny, d)
            return
        else :
            flag += 1
    # 2 step
    nx, ny = r-dx[d], c-dy[d]
    if flag == 4 :
        if board[nx][ny] != 1 :
            robot(nx, ny, d)
            return
    return

robot(r, c, d)
print(res)