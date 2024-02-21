# coding = utf-8

import sys
import math
input = sys.stdin.readline
INF = float('inf')

n = int(input())
dot = list(list(map(int,input().split())) for _ in range(n))
dot.sort(key=lambda x:x[0])

def distance(p1, p2) :
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def Closest_pair(start, end) :

    if start == end :
        return INF

    if end - start == 1 :
        return distance(dot[start], dot[end])

    mid = (start+end)//2
    distL = Closest_pair(start, mid)
    distR = Closest_pair(mid, end)
    min_d = min(distL, distR)
    dx = list()
    for i in range(start, end+1) :
        if (dot[mid][0]-dot[i][0])**2 < min_d:
            dx.append(dot[i])
    dx.sort(key=lambda x:x[1])
    for i in range(len(dx) - 1):
        for j in range(i + 1, len(dx)):
            if (dx[i][1] - dx[j][1]) ** 2 < min_d:
                min_d = min(min_d, distance(dx[i], dx[j]))
            else:
                break
    return min_d

print(Closest_pair(0, n-1))