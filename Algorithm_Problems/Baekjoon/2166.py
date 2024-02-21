# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    from collections import deque
    from itertools import *

    def getdata():
        n = int(input())
        board = list(list(map(int, input().split())) for _ in range(n))
        return n, board

    def area(board, n) :
        result = 0
        for i in range(n) :
            result += board[i][0]*board[(i+1)%n][1]
            result -= board[(i+1)%n][0]*board[i][1]
        if result < 0 :
            result = -result
        result /= 2
        return round(result, 1)

    n, board = getdata()
    print(area(board,n))