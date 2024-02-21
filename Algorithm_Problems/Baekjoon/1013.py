# coding = utf-8

import sys
input = sys.stdin.readline
import re

for _ in range(int(input())):
    tmp = input().rstrip()
    p = re.compile('(100+1+|01)+')
    if p.fullmatch(tmp):
        print("YES")
    else:
        print("NO")