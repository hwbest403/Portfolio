# coding = utf-8

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ls = list(map(int, input().split()))

def first():
    m = min(ls)
    for idx in range(len(ls)):
        if ls[idx] == m:
            ls[idx] = m+1

