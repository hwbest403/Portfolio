# coding = utf-8
import sys
input = sys.stdin.readline

MOD = 10007
N = int(input())

nCk = list(list(0 for _ in range(53)) for _ in range(53))
for n in range(53) :
    nCk[n][0], nCk[n][n] = 1, 1
    for k in range(1, n) :
        nCk[n][k] = nCk[n-1][k-1] + nCk[n-1][k]
        nCk[n][k] = nCk[n][k] % MOD
        nCk[n][n-k] = nCk[n][k]

res = 0
for i in range(4, N+1, 4) :
    if (i//4) % 2 == 1:
        res += nCk[13][i//4] * nCk[52-i][N-i]
    else :
        res -= nCk[13][i//4] * nCk[52-i][N-i]
    res = res % MOD
print(res)