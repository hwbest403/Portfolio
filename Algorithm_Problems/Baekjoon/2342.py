# coding = utf-8

import sys
input = sys.stdin.readline

ls = list(map(int,input().split()))
ls.pop()
if len(ls) == 0 :
    print(0)
    sys.exit()
dp = list(list(list(float('inf') for _ in range(5)) for _  in range(5)) for _ in range(len(ls)+1))

def moveweight(prev, next) :
    if prev == 0 :
        return 2
    elif prev == next :
        return 1
    elif abs(prev-next) == 1 or abs(prev-next) == 3 :
        return 3
    else :
        return 4

# dp 초기화 ( 초기상태 )
dp[0][0][0] = 0

# bottom up
for i, num in enumerate(ls) :
    idx = i+1
    for r in range(5) :
        for prev in range(5) :
            dp[idx][num][r] = min(dp[idx][num][r], dp[idx-1][prev][r]+moveweight(prev, num))

    for l in range(5) :
        for prev in range(5) :
            dp[idx][l][num] = min(dp[idx][l][num], dp[idx-1][l][prev]+moveweight(prev, num))

res = float('inf')
for l in range(5) :
    for r in range(5) :
        if dp[len(ls)][l][r] < res :
            res = dp[len(ls)][l][r]
print(res)