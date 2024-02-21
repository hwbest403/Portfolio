# coding = utf-8

import sys
input = sys.stdin.readline
from itertools import combinations
INF = float('inf')

n, m = map(int,input().split())
board = list(list(map(int,input().split())) for _ in range(n))
house, chicken = list(), list()
for i in range(n) :
    for j in range(n) :
        if board[i][j] == 1 :
            house.append([i,j])
        elif board[i][j] == 2 :
            chicken.append([i,j])
        else :
            pass

def distance(d1: list, d2: list) -> int:
    return abs(d1[0]-d2[0])+abs(d1[1]-d2[1])

res = INF
for choice in combinations(chicken, m) :
    t_res = 0
    for h in house :
        t_min = INF
        for c in choice :
            t_min = min(t_min, distance(h, c))
        t_res += t_min
    res = min(res, t_res)
print(res)