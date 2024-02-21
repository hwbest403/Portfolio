# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque
    from itertools import *
    import math
    T=int(input())

    for _ in range(T) :
        n = int(input())
        board = list(list(map(int, input().split())) for _ in range(n))
        total_x, total_y = 0, 0
        for i in range(n) :
            total_x += board[i][0]
            total_y += board[i][1]
        minval = 10**6
        if len(board) == 2:
            minval = math.sqrt((board[0][0]-board[1][0])**2+(board[0][1]-board[1][1])**2)
        else :
            for i in combinations([i for i in range(n)],n//2) :
                tmp_x, tmp_y = 0, 0
                for j in range(n//2) :
                    tmp_x += board[i[j]][0]
                    tmp_y += board[i[j]][1]
                tmp_x *= 2
                tmp_y *= 2
                tmpmin = math.sqrt((total_x-tmp_x)**2+(total_y-tmp_y)**2)
                if tmpmin < minval :
                    minval = tmpmin
        print(minval)