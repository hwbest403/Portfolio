# coding = utf-8

import sys
input = sys.stdin.readline

n = int(input())
g = list(map(int,input().split()))
R = list(list(map(int,input().split())) for _ in range(n))
mafia = int(input())
killed = list(False for _ in range(n))
flag = False

res = 0
def mafiagame(player, night) :
    global flag, res

    if flag :
        return

    if killed[mafia] or player == 1 :
        res = max(res, night)
        if player == 1 :
            flag = True
        return

    if player%2 :
        max_val = 0
        for i in range(n) :
            if killed[i] :
                continue
            if g[i] > max_val :
                max_val = g[i]
                target = i
        killed[target] = True
        mafiagame(player-1, night)
        killed[target] = False

    else :
        for i in range(n) :
            if i == mafia or killed[i] :
                continue
            for j in range(n) :
                g[j] += R[i][j]
            killed[i] = True
            mafiagame(player-1, night+1)
            for j in range(n) :
                g[j] -= R[i][j]
            killed[i] = False

mafiagame(n,0)
print(res)