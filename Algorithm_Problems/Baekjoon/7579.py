# coding = utf-8

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
mem = [0] + list(map(int,input().split()))
cost = [0] + list(map(int,input().split()))
dp = list(list(0 for _ in range(sum(cost)+1)) for _ in range(n+1))

ans = float('inf')
for i in range(1, n+1) :
    for j in range(1, sum(cost)+1) :
        if j < cost[i] :
            dp[i][j] = dp[i-1][j]
            continue
        dp[i][j] = max(dp[i-1][j-cost[i]]+mem[i], dp[i-1][j])
        if dp[i][j] >= m :
            if j < ans :
                ans = j

print(ans)