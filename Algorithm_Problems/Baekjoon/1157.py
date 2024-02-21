# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque
    from itertools import *


    def getdata():
        n = input().rstrip()
        return n

    a = getdata()
    a = a.upper()
    a_list = list(set(a))
    cnt = list()
    for i in a_list :
        count = a.count(i)
        cnt.append(count)
    if cnt.count(max(cnt)) >= 2:
        print("?")
    else :
        print(a_list[(cnt.index(max(cnt)))])