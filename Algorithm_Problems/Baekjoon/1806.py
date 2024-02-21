# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque
    from itertools import *

    def getdata():
        n, s = map(int,input().split())
        board = list(map(int, input().split()))
        return n, s, board

    def tp(board, n, s) :
        lp, rp = 0, 0
        tmpsum = board[rp]
        minval = n+1
        while True :
            # print(lp,rp,tmpsum, end=' ')
            if tmpsum < s :
                rp += 1
                if rp == n :
                    break
                tmpsum += board[rp]
            else :
                if lp == rp :
                    minval = 1
                    break
                else :
                    if rp - lp + 1 < minval :
                        minval = rp - lp + 1
                    lp += 1
                    tmpsum -= board[lp-1]
        if minval == n+1 :
            minval = 0
        return minval

    n, s, board = getdata()
    print(tp(board,n,s))