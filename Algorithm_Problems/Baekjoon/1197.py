# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque
    from itertools import *

    v, e = map(int,input().split())
    board = list(list(map(int,input().split())) for _ in range(e))
    board.sort(key=lambda x:x[2])
    total_weight = 0
    root = [i for i in range(v+1)]

    def find(node) :
        if root[node] == node:
            return node
        root[node] = find(root[node])
        return root[node]

    def union(a, b) :
        a, b = find(a), find(b)
        if a>b :
            root[a]=b
        else :
            root[b] = a

    total_weight = 0

    for item in board:
        print(root)
        lv, rv, w = item[0], item[1], item[2]
        if find(lv) != find(rv) :
            union(lv,rv)
            total_weight += w

    print(total_weight)

