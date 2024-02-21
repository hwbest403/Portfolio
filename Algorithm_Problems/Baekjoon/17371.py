# coding = utf-8

import sys
input = sys.stdin.readline
import math
INF = float('inf')

n = int(input())
dot = list(list(map(int,input().split())) for _ in range(n))

def Euclid_distance(dot1, dot2) :
    return math.sqrt((dot1[0]-dot2[0])**2+(dot1[1]-dot2[1])**2)

res = INF
res_x, res_y = 0, 0
for h in dot :
    tmp_max, tmp_min = -INF, INF
    for d in dot :
        tmp_d = Euclid_distance(h, d)
        if tmp_max < tmp_d :
            tmp_max = tmp_d
        if tmp_d < tmp_min :
            tmp_min = tmp_d
    if (tmp_min+tmp_max)/2 < res :
        res = (tmp_min+tmp_max)/2
        res_x, res_y = h[0], h[1]
print(res_x, res_y)