# coding = utf-8

import sys
input = sys.stdin.readline
from collections import defaultdict

r, c, k = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(3))

def sorting(ls):
    gp = defaultdict(int)
    for n in ls:
        if n != 0:
            gp[n] += 1
    gp = sorted(gp.items(), key=lambda x:(x[1],x[0]))
    re = list()
    for l in gp:
        re.append(l[0])
        re.append(l[1])
    return re, len(re)

maxv = 0
for i in range(len(A)):
    A[i], tp = sorting(A[i])
    if tp>maxv:
        maxv = tp

for i in range(len(A)):
    if maxv > 100:
        maxv = 100
    while len(A[i]) < maxv:
        A[i].append(0)
    if len(A[i]) > 100:
        while len(A[i]) > 100:
            A[i].pop()

for i in range(maxv):
    for j in range(len(A)):
        A[j][i]

