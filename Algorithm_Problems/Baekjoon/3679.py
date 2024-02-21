# coding = utf-8
import sys
from functools import cmp_to_key
import math
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    tmp = list(map(int,input().split()))
    n, tmp = tmp[0], tmp[1:]
    dot = list()
    flag = 1
    tmp_dot = list()
    idx = 0
    for num in tmp :
        if flag == 1:
            tmp_dot.append(num)
            flag += 1
        else :
            tmp_dot.append(num)
            tmp_dot.append(idx)
            idx += 1
            dot.append(tmp_dot)
            flag = 1
            tmp_dot = list()

    def distance(p1, p2) :
        return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

    def ccw(p1, p2, p3) :
        return p2[0]*p3[1]-p2[1]*p3[0]-p1[0]*p3[1]+p1[1]*p3[0]+p1[0]*p2[1]-p1[1]*p2[0]

    dot.sort(key=lambda x:(x[1], x[0]))
    pivot = dot[0]

    def comp(p1, p2) :
        if ccw(pivot, p1, p2) > 0 :
            return -1
        else :
            return 1

    def comp2(p1,p2) :
        if distance(pivot, p1) > distance(pivot, p2) :
            return -1
        else :
            return 1

    dot[1:]=sorted(dot[1:],key=cmp_to_key(comp))
    endidx = -1
    for i in range(len(dot)-1,0,-1) :
        if ccw(pivot,dot[i],dot[i-1]) != 0 :
            break
        else :
            endidx = i-1
    if endidx != -1 :
        dot[endidx:]=sorted(dot[endidx:],key=cmp_to_key(comp2))
    # print(dot)
    for d in dot :
        print(d[2], end=" ")