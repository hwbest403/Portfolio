# coding = utf-8

import sys
input = sys.stdin.readline

n, l = map(int,input().split())
board = list(list(map(int,input().split())) for _ in range(n))

def check(ls) :
    visited = list(False for _ in range(len(ls)))
    for idx, num in enumerate(ls) :
        if idx == len(ls)-1 :
            return True
        if abs(num-ls[idx+1]) >= 2 :
            return False
        if num < ls[idx+1] :
            for i in range(l) :
                tmp = idx-i
                if tmp < 0 :
                    return False
                if visited[tmp] :
                    return False
                else :
                    visited[tmp] = True
        elif num > ls[idx+1] :
            for i in range(1, l+1) :
                tmp = idx+i
                if tmp >= n :
                    return False
                if visited[tmp] :
                    return False
                else :
                    visited[tmp] = True
        else :
            pass

res = 0
for ls in board :
    if check(ls) :
        res += 1
for i in range(n) :
    tmp = list()
    for j in range(n) :
        tmp.append(board[j][i])
    if check(tmp) :
        res += 1
print(res)