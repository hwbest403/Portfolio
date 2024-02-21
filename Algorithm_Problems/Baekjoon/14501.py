# coding = utf-8

import sys
input = sys.stdin.readline

n = int(input())
ls = list(list(map(int,input().split())) for _ in range(n))
dp = list(0 for _ in range(n+1))

for idx, ele in enumerate(ls) :
    for i in range(idx+ele[0], n+1) :
        dp[i] = max(dp[i], dp[idx]+ele[1])
print(dp[-1])