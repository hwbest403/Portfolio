# coding = utf-8

if __name__ == '__main__':
    import sys
    import math
    input = sys.stdin.readline
    from collections import deque
    from itertools import *


    def getdata():
        a, b, v = map(int,input().split())
        return a, b, v

    a,b,v = getdata()
    o = a-b
    print(math.ceil(((v-a)/o))+1)