# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque
    from itertools import *


    def getdata():
        n = int(input())
        board = list(list(map(int, input().split())) for _ in range(2))
        return n, board

    def sol(n, board) :
        dp = list(list(0 for _ in range(n)) for _ in range(2))
        dp[0][0], dp[1][0] = board[0][0], board[1][0]
        if n != 1 :
            dp[0][1], dp[1][1] = board[1][0] + board[0][1], board[0][0] + board[1][1]
            for i in range(2, n) :
                dp[0][i] = max(dp[0][i-2] + board[1][i-1] + board[0][i], dp[1][i-2] + board[0][i], dp[1][i-1] + board[0][i])
                dp[1][i] = max(dp[1][i-2] + board[0][i-1] + board[1][i], dp[0][i-2] + board[1][i], dp[0][i-1] + board[1][i])
        print(max(dp[0][n-1], dp[1][n-1]))

    T = int(input())
    for _ in range(T) :
        n, board = getdata()
        sol(n, board)