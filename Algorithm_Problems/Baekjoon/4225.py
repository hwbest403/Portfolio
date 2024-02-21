# coding = utf-8

import sys
input = sys.stdin.readline

idx = 0
while True :
    idx += 1
    n = int(input())
    if n == 0 :
        break
    dot = list(list(map(int,input().split())) for _ in range(n))

    res = 0
    print(f"Case {idx}: {res}")