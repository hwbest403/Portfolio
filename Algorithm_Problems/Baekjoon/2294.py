# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque
    from itertools import *


    def getdata():
        n, k = map(int,input().split())
        board = list(int(input()) for _ in range(n))
        return n, k, board

    n, k, board = getdata()
    dp = [0] * (k+1)
    for c in board :
        if c<=k :
            dp[c] = 1
    # print(dp)
    for i in range(1, k+1) :
        # print(f"=={i}")
        tmp = 10**6
        for c in board :
            if 0<=i-c :
                tmp = min(tmp, dp[i-c])
        dp[i] = tmp + 1
    if dp[k] == 10**6+1 :
        print(-1)
    else :
        print(dp[k])