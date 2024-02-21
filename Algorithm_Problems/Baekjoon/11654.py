# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque
    from itertools import *


    def getdata():
        a = input().rstrip()
        return a

    a = getdata()
    if type(a) == type("A") :
        print(ord(a))
    else :
        print(chr(a))