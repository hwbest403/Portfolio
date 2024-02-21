# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    from collections import deque
    from itertools import *

    def getdata():
        n, m = map(int, input().split())
        board = list(list(map(int, input().split())) for _ in range(m))
        return n, m, board

    n, m, board = getdata()
    for i in range(m) :
        board[i][0] = board[i][0] - 1
        board[i][1] = board[i][1] - 1
    board.sort(key=lambda x:x[2])
    par = [i for i in range(n)]

    def find(a) :
        if par[a] == a :
            return a
        else :
            par[a] = find(par[a])
            return par[a]

    def union(a, b) :
        a, b = find(a), find(b)
        if a>b :
            par[a] = b
        else :
            par[b] = a

    total_weight = 0
    maxval = 0
    for ele in board :
        lv, rv, w = ele[0], ele[1], ele[2]
        if find(lv) != find(rv) :
            union(lv, rv)
            total_weight += w
            if w > maxval :
                maxval = w

    print(total_weight-maxval)