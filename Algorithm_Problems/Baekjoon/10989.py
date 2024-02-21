# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque
    from itertools import *


    def getdata():
        n = int(input())
        return n

    n = getdata()
    board = list(0 for _ in range(10001))
    for i in range(n) :
        tmp = int(input())
        board[tmp] += 1
    total = 0
    for i in range(10001) :
        if board[i] != 0 :
            for _ in range(board[i]) :
                print(i)
                total += 1
        if total == n :
            break
