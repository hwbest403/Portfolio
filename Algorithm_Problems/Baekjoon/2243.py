# coding = utf-8

import sys
input = sys.stdin.readline
from bisect import bisect_right

n = int(input())

def num_in(ls, num) :
    bisect_right(ls, num)
    return

def num_out(ls, num, k) :

    return

box = list()
for _ in range(n) :
    tmp = list(map(int,input().split()))
    if tmp[0] == 1 :
        num_in(box, tmp[1])
    else :
        num_out(box, tmp[1], tmp[2])
    print(box)