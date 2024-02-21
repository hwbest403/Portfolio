# coding = utf-8

import sys
input = sys.stdin.readline

n = int(input())
ls = list(list(map(int,input().split())) for _ in range(n))

dp = list(list(0 for  _ in range(n)) for _ in range(n))
# dp[start][end], 초기화 dp[i][i] = 0
for i in range(n) :
    dp[i][i] = 0
for len in range(1, n) :
    for start in range(n-len) :
        end = start + len
        dp[start][end] = 2**32
        for i in range(start, end) :
            dp[start][end] = min(dp[start][end], dp[start][i] + dp[i+1][end] + ls[start][0]*ls[i][1]*ls[end][1])

print(dp[0][-1])