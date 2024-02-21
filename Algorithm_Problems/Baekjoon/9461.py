# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque
    from itertools import *


    def getdata():
        n = int(input())
        board = list(int(input()) for _ in range(n))
        return n, board

    n, board = getdata()

    dp=[1] * 100
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    dp[4] = 2
    for i in range(5, 100) :
        dp[i] = dp[i-1] + dp[i-5]
    for i in board :
        print(dp[i-1])