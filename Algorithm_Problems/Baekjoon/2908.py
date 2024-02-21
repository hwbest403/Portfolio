# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque
    from itertools import *


    def getdata():
        n = list(map(int,input().split()))
        return n

    board = getdata()
    result = list()
    for i in board :
        tmp1 = i % 10
        i = i//10
        tmp2 = i % 10
        i = i//10
        result.append(tmp1*100+tmp2*10+i)
    print(max(result))