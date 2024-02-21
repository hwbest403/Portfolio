# coding = utf-8

if __name__ == '__main__':
    import sys
    import copy
    input = sys.stdin.readline
    from collections import deque

    def getdata():
        m, n, h = map(int,input().split())
        board = list(list(map(int, input().split())) for _ in range(n))
        return n, m, h, board

    n, m, h, board = getdata()
    need_visited, visited, dis = deque(), deque(), dict()
