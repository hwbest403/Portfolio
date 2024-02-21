import sys
input = sys.stdin.readline

INF = float('inf')
n = int(input())
weight = list(list(map(int,input().split())) for _ in range(n))
dp = list(list(INF for _ in range(1<<n)) for _ in range(n))

def hamilton(start, visited) :
    if dp[start][visited] != INF:
        return dp[start][visited]

    if visited == (1<<n)+1 :
        if weight[start][0] :
            return weight[start][0]
        else :
            return INF

    for i in range(1, n) :
        if not weight[start][i] :
            continue
        if visited & (1<<i) :
            continue
        dp[start][visited] = min(dp[start][visited], hamilton(i, visited|(1<<i))+weight[start][i])

    return dp[start][visited]

print(hamilton(0, 1))
print(dp)