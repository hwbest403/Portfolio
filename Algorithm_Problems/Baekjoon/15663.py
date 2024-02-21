# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    from itertools import *

    def getdata():
        n, m = map(int,input().split())
        board = list(map(int, input().split()))
        return n, m, board

    n, m, board = getdata()
    board.sort(reverse=False)
    tmp = list()
    for case in product(board, repeat=m) :
        print(*case)