# coding = utf-8

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
medal = list(list(map(int,input().split())) for _ in range(n))

medal.sort(key=lambda x:(x[1], x[2], x[3]), reverse=True)
res = 1
flag = 1
for idx in range(n) :
    if idx != 0 :
        if medal[idx-1][1:] == medal[idx][1:] :
            flag += 1
        else :
            res += flag
            flag = 1
    if medal[idx][0] == k :
        print(res)