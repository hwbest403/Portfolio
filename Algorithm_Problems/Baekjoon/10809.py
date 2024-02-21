# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque
    from itertools import *


    def getdata():
        n = input().rstrip()
        return n

    a = getdata()
    board = list(-1 for _ in range(26))
    for i in range(len(a)):
        tmp = ord(a[i]) - 97
        if board[tmp] == -1:
            board[tmp] = i
    for i in range(len(board)):
        print(board[i], end=" ")