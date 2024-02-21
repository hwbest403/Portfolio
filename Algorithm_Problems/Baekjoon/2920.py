# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque
    from itertools import *


    def getdata():
        n = list(map(int, input().split()))
        return n

    board = getdata()
    if board == sorted(board, reverse=True) :
        print("descending")
    elif board == sorted(board, reverse=False) :
        print("ascending")
    else :
        print("mixed")