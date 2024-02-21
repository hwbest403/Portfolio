# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque
    from itertools import *

    def getdata():
        n = int(input())
        board = list(list(map(int, input().split())) for _ in range(n))
        return n ,board

    def mintunnel(board, start, need_visited) :
        res = 3*(10**9)
        next = -1
        for node in need_visited :
            tmp = min(abs(board[start][0]-board[node][0]), abs(board[start][1]-board[node][1]), abs(board[start][2]-board[node][2]))
            if tmp < res :
                res = tmp
                next = node
        return res, next

    n, board = getdata()
    visited = [0]
    need_visited=list(i for i in range(1, n))
    res = 0
    while need_visited :
        minval, next = 3*(10**9), -1
        for node in visited :
            tmp1, tmp2 = mintunnel(board, node, need_visited)
            if tmp1 < minval :
                minval = tmp1
                next = tmp2
        res += minval
        visited.append(next)
        need_visited.remove(next)
    print(res)