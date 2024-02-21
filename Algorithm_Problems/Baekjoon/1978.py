# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque
    from itertools import *


    def getdata():
        n = int(input())
        board = list(map(int, input().split()))
        return n, board

    def prime(p) :
        tmp = list()
        for i in range(1,p+1) :
            if p%i == 0 :
                tmp.append(i)
        if len(tmp) == 2:
            return True
        else :
            return False

    n, board = getdata()
    cnt = 0
    for i in range(n) :
        if prime(board[i]) :
            cnt+=1
    print(cnt)