# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque
    from itertools import *


    def getdata():
        n = int(input())
        board = list(list(map(int, input().split())) for _ in range(n))
        return
