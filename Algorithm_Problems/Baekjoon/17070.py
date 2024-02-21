# coding = utf-8

import sys
input = sys.stdin.readline

n = int(input())
board = list(list(map(int, input().split())) for _ in range(n))
dp_g = list(list(0 for _ in range(n)) for _ in range(n))
dp_s = list(list(0 for _ in range(n)) for _ in range(n))
dp_d = list(list(0 for _ in range(n)) for _ in range(n))
dp = list(list(0 for _ in range(n)) for _ in range(n))
dp_g[0][1] = 1
for i in range(n):
    for j in range(2, n):
        dp_g[i][j] = dp_g[i]