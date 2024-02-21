import sys
from itertools import product
from copy import deepcopy

input = sys.stdin.readline

def getdata():
    n, m = map(int, input().split())
    board = list(list(map(int, input().split())) for _ in range(n))
    return n, m, board

def printboard(board):
    for row in board:
        print(row)
    return

def findcctv(board, n, m):
    cctv_info = list()
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and board[i][j] != 6:
                cctv_info.append((i, j, board[i][j]))
            if board[i][j] == 0 :
                cnt += 1
    return cctv_info, cnt

def move(board, x, y, d, n, m):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    nx, ny = x+dx[d], y+dy[d]
    if 0<=nx<n and 0<=ny<m and board[nx][ny] != 6:
        return True, nx, ny
    else:
        return False, x, y

def moveall(board, x, y, d, n, m):
    cnt = 0
    while True:
        flag, x, y = move(board, x, y, d, n, m)
        if not flag:
            break
        if board[x][y] == 0:
            board[x][y] = '#'
            cnt += 1
    return board, cnt

def masking(board, cctv_info, case, n, m):
    cnt = 0
    # print(case)
    # print()
    for idx, dir in enumerate(case):
        x, y, c = cctv_info[idx]
        if c == 1:
            board, count = moveall(board, x, y, dir, n, m)
            cnt += count
        if c == 2:
            board, count = moveall(board, x, y, dir, n, m)
            cnt += count
            board, count = moveall(board, x, y, (dir+2)%4, n, m)
            cnt += count
        if c == 3:
            board, count = moveall(board, x, y, dir, n, m)
            cnt += count
            board, count = moveall(board, x, y, (dir+1)%4, n, m)
            cnt += count
        if c == 4:
            board, count = moveall(board, x, y, dir, n, m)
            cnt += count
            board, count = moveall(board, x, y, (dir + 1) % 4, n, m)
            cnt += count
            board, count = moveall(board, x, y, (dir + 2) % 4, n, m)
            cnt += count
        if c == 5:
            board, count = moveall(board, x, y, dir, n, m)
            cnt += count
            board, count = moveall(board, x, y, (dir + 1) % 4, n, m)
            cnt += count
            board, count = moveall(board, x, y, (dir + 2) % 4, n, m)
            cnt += count
            board, count = moveall(board, x, y, (dir + 3) % 4, n, m)
            cnt += count
    # printboard(board)
    # print(cnt)
    # print()
    return cnt

def sol():
    answer = -1
    n, m, board = getdata()
    cctv_info, zero_cnt = findcctv(board, n, m)
    cctv_cnt = len(cctv_info)
    for case in product([0, 1, 2, 3], repeat = cctv_cnt):
        print(case)
        mask_cnt = masking(deepcopy(board), cctv_info, case, n, m)
        if mask_cnt > answer:
            answer = mask_cnt
    return zero_cnt-answer

print(sol())