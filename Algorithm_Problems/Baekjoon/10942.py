# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque
    from itertools import *


    def getdata():
        n = int(input())
        board = list(map(int,input().split()))
        return n, board

    def makepalindrome(board, n) :
        dp = list(list(0 for _ in range(n)) for _ in range(n))
        for i in range(n) :
            dp[i][i] = 1
            if i != n-1 and board[i] == board[i+1] :
                dp[i][i+1] = 1
        for jump in range(2, n) :
            for left in range(n-jump) :
                right = left + jump
                if board[left] == board[right] and dp[left+1][right-1] == 1 :
                    dp[left][right] = 1
        return dp

    n, board= getdata()
    dp = makepalindrome(board,n)
    m = int(input())
    for i in range(m) :
        s, e = map(int,input().split())
        print(dp[s-1][e-1])
