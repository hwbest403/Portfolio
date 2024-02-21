# coding = utf-8
import sys
input = sys.stdin.readline

n = int(input())
board = list(list(map(int, input().split())) for _ in range(n))

dp = list(list(0 for _ in range(n)) for _ in range(n))
dp[0][0] = 1
for i in range(n) :
    for j in range(n) :
        jump = board[i][j]
        if jump == 0 :
            continue
        if i+jump<n :
            dp[i+jump][j] += dp[i][j]
        if j+jump<n :
            dp[i][j+jump] += dp[i][j]

for row in dp:
    print(row)

print(dp[-1][-1])