# coding = utf-8

import sys
input = sys.stdin.readline

while True :
    histo = list(map(int,input().split()))
    n = histo[0]
    if not n :
        break
    histo = histo[1:]
    stack = list()
    maxval = -1
    for i in range(n) :
        if not stack :
            stack.append([i, histo[i]])
            continue
        while stack and stack[-1][1] > histo[i] :
            tmp = stack.pop()
            if stack :
                tmp_area = tmp[1]*((i-1)-stack[-1][0])
            else :
                tmp_area = tmp[1]*i
            if tmp_area > maxval :
                maxval = tmp_area
        stack.append([i, histo[i]])
    while stack :
        tmp = stack.pop()
        if stack:
            tmp_area = tmp[1] * ((n - 1) - stack[-1][0])
        else:
            tmp_area = tmp[1] * n
        if tmp_area > maxval:
            maxval = tmp_area
    print(maxval)