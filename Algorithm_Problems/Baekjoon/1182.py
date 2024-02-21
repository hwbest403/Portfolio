# coding = utf-8

import sys
input = sys.stdin.readline
from itertools import combinations

n, s = map(int, input().split())
ls = list(map(int, input().split()))

res = 0
for i in range(1, n+1) :
    for choice in combinations(ls, i) :
        print(choice)
        if sum(choice) == s:
            res += 1

print(res)