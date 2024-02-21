# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    from collections import deque
    from itertools import *


    def getdata():
        k = int(input())
        n = int(input())
        return n, k

    T = int(input())

    for _ in range(T) :
        n, k = getdata()
        board = list(list(0 for _ in range(n+1)) for _ in range(k+1))
        for i in range(n+1) :
            board[0][i] = i
        for i in range(1, k+1) :
            for j in range(n+1) :
                board[i][j] = board[i][j-1] + board[i-1][j]
        print(board[k][n])