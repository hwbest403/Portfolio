# coding = utf-8

import sys
input = sys.stdin.readline
from itertools import product
import copy

direc = ['U','D','L','R']

n = int(input())
board = list(list(map(int,input().split())) for _ in range(n))

def erasezero(ls) :
    res = list()
    while ls :
        if ls[0] != 0 :
            res.append(ls[0])
            del ls[0]
        else :
            del ls[0]
    while True :
        if len(res) == n :
            break
        res.append(0)
    return res

def makesum(ls) :
    res = list()
    while ls :
        if ls[0] == 0 :
            break
        else :
            if len(res) == 0 :
                res.append([ls[0], 0])
                del ls[0]
            else :
                if res[-1][0] != ls[0] :
                    res.append([ls[0], 0])
                    del ls[0]
                else :
                    if res[-1][1] == 0 :
                        res[-1][0] *= 2
                        res[-1][1] = 1
                        del ls[0]
                    else :
                        res.append([ls[0], 0])
                        del ls[0]
    rres = list()
    while res :
        rres.append(res[0][0])
        del res[0]
    while True :
        if len(rres) == n :
            break
        rres.append(0)
    return rres

def movebox(board, dir) :
    if dir == 'U' :
        for i in range(n) :
            tp = list()
            for j in range(n) :
                tp.append(board[j][i])
            tp = makesum(erasezero(tp))
            for j in range(n-1,-1,-1) :
                board[j][i] = tp.pop()
    elif dir == 'D' :
        for i in range(n) :
            tp = list()
            for j in range(n-1,-1,-1) :
                tp.append(board[j][i])
            tp = makesum(erasezero(tp))
            for j in range(n) :
                board[j][i] = tp.pop()
    elif dir == 'L' :
        for idx, row in enumerate(board) :
            tp = makesum(erasezero(row))
            board[idx] = tp
    else :
        for idx, row in enumerate(board) :
            tp = makesum(erasezero(row[::-1]))
            board[idx] = tp[::-1]
    return board

def maxboard(board) :
    res = 0
    for row in board :
        for num in row :
            res = max(res, num)
    return res

ans = 0
for choice in product(list(i for i in range(4)), repeat=5) :
    copy_board = copy.deepcopy(board)
    for dir in choice :
        copy_board = movebox(copy_board, direc[dir])
    ans = max(ans, maxboard(copy_board))
print(ans)