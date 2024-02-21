# https://www.acmicpc.net/problem/1018

if __name__ == '__main__' :
    from collections import deque
    from itertools import *
    import sys
    import copy

    input = sys.stdin.readline
    def printboard(board, n):
        for i in range(n):
            print(board[i])


    n, m = list(map(int, input().split()))
    board = list(list(map(str, input())) for _ in range(n))


    def findcolor(board, x, y):
        cnt1, cnt2 = 0, 0
        for i in range(8):
            for j in range(8):
                if i == 0 and j == 0:
                    ic = board[x + i][y + j]
                if (i + j) % 2 == 0 and board[x + i][y + j] != ic:
                    cnt1 += 1
                if (i + j) % 2 != 0 and board[x + i][y + j] == ic:
                    cnt1 += 1
                if (i + j) % 2 == 0 and board[x + i][y + j] == ic:
                    cnt2 += 1
                if (i + j) % 2 != 0 and board[x + i][y + j] != ic:
                    cnt2 += 1
        if cnt1 < cnt2:
            return cnt1
        else:
            return cnt2


    def sol(board):
        copy_board = copy.deepcopy(board)
        min = 2500
        for i in range(n):
            copy_board[i].pop()
            if i + 7 >= n:
                break
            for j in range(m):
                if j + 7 >= m:
                    break
                tmp = findcolor(copy_board, i, j)
                if tmp < min:
                    min = tmp
        print(min)
    sol(board)
