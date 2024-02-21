# coding = utf-8

import sys
input = sys.stdin.readline
import heapq
import copy

n = int(input())
board = list(sorted(list(map(int,input().split()))) for _ in range(n))
d = int(input())
board.sort(key=lambda x:x[1])

def sol() :
    res = -1
    hq = list()
    for ls in board :
        if ls[0] >= ls[1] - d :
            heapq.heappush(hq, ls)
        while hq and hq[0][0] < ls[1] - d :
            heapq.heappop(hq)
        res = max(res, len(hq))
    return res

print(sol())