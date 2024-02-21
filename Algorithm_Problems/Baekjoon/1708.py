# coding = utf-8
import sys
from functools import cmp_to_key
input = sys.stdin.readline

n = int(input())
dot = list(list(map(int,input().split())) for _ in range(n))

def outerproduct(p1, p2, p3) :
    return p2[0]*p3[1]-p2[1]*p3[0]-p1[0]*p3[1]+p1[1]*p3[0]+p1[0]*p2[1]-p1[1]*p2[0]

def ccw(p1, p2, p3) :
    if outerproduct(p1,p2,p3) > 0 :
        return True
    else :
        return False

dot.sort(key=lambda x:(x[1], x[0]))
pivot = dot[0]
res = list()
res.append(pivot)

def comp(p1, p2) :
    if ccw(pivot, p1, p2) :
        return -1
    else :
        return 1

dot.sort(key=cmp_to_key(comp))
res.append(dot[1])
for i in range(2, n) :
    while len(res) >= 2 :
        second = res.pop()
        first = res[-1]
        if ccw(first,second,dot[i]) :
            res.append(second)
            break
    res.append(dot[i])
print(len(res))