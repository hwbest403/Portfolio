N = int(input())
pages = list(map(int, input().split()))
dp = [[0]*N for _ in range(N)]

# 2개 이하 최소비용 갱신
for i in range(N):
    dp[i][i] = 0
    if i < N-1:
        dp[i][i+1] = pages[i]+pages[i+1]

# print(dp)

# 3개 이상 최소비용 갱신 (→ ↑ 방향)
for i in range(N-1, -1, -1):
    for j in range(N):
        if i+1 < j:
            # dp[i][j] = i~j 최소비용 = min([i][i~(j-1)]+[(i+1)~j][j])
            dp[i][j] = min(dp[i][k] + dp[k+1][j] for k in range(i, j)) + sum(pages[i:j+1])
for row in dp:
    print(row)