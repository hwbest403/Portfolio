# coding = utf-8

import sys
input = sys.stdin.readline
from collections import deque

ls = list(deque(input().rstrip()) for _ in range(4))
k = int(input())
ro = list(list(map(int,input().split())) for _ in range(k))

def rot(id, dir) :
    visited = list(False for _ in range(3))
    for i in range(3) :
        if ls[i][2] != ls[i+1][6] :
            visited[i] = True
    ls[id].rotate(dir)
    tmp_id, tmp_dir = id, dir
    while True :
        tmp_id += 1
        tmp_dir = -tmp_dir
        if tmp_id >= 4 :
            break
        if visited[tmp_id-1] :
            ls[tmp_id].rotate(tmp_dir)
        else :
            break
    tmp_id, tmp_dir = id, dir
    while True :
        tmp_id -= 1
        tmp_dir = -tmp_dir
        if tmp_id < 0:
            break
        if visited[tmp_id]:
            ls[tmp_id].rotate(tmp_dir)
        else:
            break

for r in ro :
    rot(r[0]-1, r[1])
res = 0
for i, t in enumerate(ls) :
    if t[0] == '1' :
        res += 1<<i
print(res)