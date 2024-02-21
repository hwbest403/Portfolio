# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque
    from itertools import *


    def getdata():
        n = map(int,input().split())
        return n

    board = getdata()
    res = 0
    for i in board :
        res += i**2
    res = res % 10
    print(res)