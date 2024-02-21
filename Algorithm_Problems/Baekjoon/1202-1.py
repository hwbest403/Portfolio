# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque
    from itertools import *
    import queue

    N, K = input().split()
    N = int(N)
    K = int(K)
    A = []
    for i in range(N):
        x, y = input().split()
        x = int(x)
        y = int(y)
        A.append([x, y])
    for i in range(K):
        A.append([int(input()), 2000000])
    A.sort()
    print(A)
    ans = 0
    pq = queue.PriorityQueue(N)
    for x in A:
        if x[1] != 2000000:
            pq.put(-x[1])
        else:
            if not pq.empty():
                print(pq)
                t = -pq.get()
                print(t)
                ans += t
    print(ans)
