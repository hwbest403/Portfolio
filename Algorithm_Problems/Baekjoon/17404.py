# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque
    from itertools import *

    def getdata():
        n = int(input())
        board = list(list(map(int,input().split())) for _ in range(n))
        return n, board

    n, board = getdata()
    dp = list(list(0 for _ in range(3)) for _ in range(n))
    res = 0
    for j in range(3) :
        dp[0][j]=board[0][j]
        dp[1][j] = 10**6
        dp[1][(j+1)%3] = dp[0][j] + board[1][(j+1)%3]
        dp[1][(j+2)%3] = dp[0][j] + board[1][(j+2)%3]
        for i in range(2, n):
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + board[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + board[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + board[i][2]
        minval = min(dp[n-1][(j+1)%3], dp[n-1][(j+2)%3])
        if j == 0 :
            res = minval
        else :
            if minval < res :
                res = minval
    print(res)