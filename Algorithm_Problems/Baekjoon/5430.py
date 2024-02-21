# coding = utf-8

import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    command = list(input().rstrip())
    n = int(input())
    ls = input().rstrip()[1:-1].split(',')
    if n == 0:
        ls = deque()
    else:
        ls = deque(ls)
    e_flag = True
    r_flag = True
    for c in command:
        if c == 'R' and r_flag:
            r_flag = False
        elif c == 'R' and not r_flag:
            r_flag = True
        if c == 'D':
            if len(ls) == 0:
                e_flag = False
                print("error")
                break
            else:
                if r_flag:
                    ls.popleft()
                else:
                    ls.pop()
    if e_flag:
        if r_flag:
            print("["+",".join(ls)+"]")
        else:
            ls.reverse()
            print("["+",".join(ls)+"]")