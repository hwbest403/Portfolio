# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    from itertools import *

    def getdata():
        n, m = map(int, input().split())
        return n, m

    n, m = getdata()
    for case in combinations_with_replacement([i+1 for i in range(n)], m) :
        print(*case)