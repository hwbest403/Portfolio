# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque
    from itertools import *

    def getdata():
        n = int(input())
        board = list(int(input()) for _ in range(n))
        return n ,board

    n, board = getdata()
    board.sort(reverse=False)
    for i in range(n) :
        print(board[i])