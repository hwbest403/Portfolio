# coding = utf-8

import sys
input = sys.stdin.readline
import copy

n, m, t = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(n))
r = lambda x, y: 0 <= x < n and 0 <= y < m
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    if board[i][0] == -1:
        air = i
        break

def diffusion():
    copy_board = copy.deepcopy(board)
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 5:
                for d in range(4):
                    nx, ny = i+dx[d], j+dy[d]
                    if r(nx, ny) and board[nx][ny] != -1:
                        copy_board[nx][ny] += (board[i][j]//5)
                        copy_board[i][j] -= (board[i][j]//5)
    return copy_board

def turnon(air):
    for i in range(air-1, 0, -1):
        board[i][0] = board[i-1][0]
    for i in range(m-1):
        board[0][i] = board[0][i+1]
    for i in range(air):
        board[i][m-1] = board[i+1][m-1]
    for i in range(m-1, 1, -1):
        board[air][i] = board[air][i-1]
    board[air][1] = 0
    for i in range(air+2, n-1):
        board[i][0] = board[i+1][0]
    for i in range(m-1):
        board[n-1][i] = board[n-1][i+1]
    for i in range(n-1, air+1, -1):
        board[i][m-1] = board[i-1][m-1]
    for i in range(m-1, 1, -1):
        board[air+1][i] = board[air+1][i-1]
    board[air+1][1] = 0

def summise():
    res = 0
    for row in board:
        for num in row:
            if num > 0:
                res += num
    return res

for _ in range(t):
    board = diffusion()
    turnon(air)

print(summise())