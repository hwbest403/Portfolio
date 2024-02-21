# coding = utf-8

import sys
input = sys.stdin.readline

ls = list(list(input().rstrip()) for _ in range(2))
l1, l2 = len(ls[0]), len(ls[1])

dp = list(list(0 for _ in range(l2+1)) for _ in range(l1+1))
for i in range(1, l1+1):
    for j in range(1, l2+1):
        if ls[0][i-1] == ls[1][j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])