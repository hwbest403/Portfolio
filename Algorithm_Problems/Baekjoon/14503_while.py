# coding = utf-8

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(n))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def sol(r, c, d):
    res = 0
    nx, ny = r, c
    while True:
        # 1 step
        print()
        for row in board:
            print(row)
        if board[nx][ny] == 0:
            board[nx][ny] = 2
            res += 1
        # 3 step
        flag = 0
        for _ in range(4):
            d -= 1
            d %= 4
            nx, ny = nx+dx[d], ny+dy[d]
            if board[nx][ny] == 0:
                break
            else:
                nx, ny = nx-dx[d], ny-dy[d]
                flag += 1
        if flag < 4:
            continue
        # 2 step
        if flag == 4:
            nx, ny = nx-dx[d], ny-dy[d]
            if board[nx][ny] == 1:
                return res

print(sol(r, c, d))