# coding = utf-8

import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
s3 = input().rstrip()
l1, l2, l3 = len(s1), len(s2), len(s3)

dp = list(list(list(0 for _ in range(l3+1)) for _ in range(l2+1)) for _ in range(l1+1))

res = -1
for i in range(1, l1+1):
    for j in range(1, l2+1):
        for k in range(1, l3+1):
            if s1[i-1] == s2[j-1] and s2[j-1] == s3[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                if res < dp[i][j][k]:
                    res = dp[i][j][k]
print(res)