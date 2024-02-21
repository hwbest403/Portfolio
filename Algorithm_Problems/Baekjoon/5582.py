# coding = utf-8

import sys
input = sys.stdin.readline

ls1 = input().rstrip()
ls2 = input().rstrip()
dp = list(list(0 for _ in range(len(ls2)+1)) for _ in range(len(ls1)+1))

res = 0
for i in range(1, len(ls1)+1):
    for j in range(1, len(ls2)+1):
        if ls1[i-1] == ls2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            if dp[i][j] > res:
                res = dp[i][j]

print(res)