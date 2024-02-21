# coding = utf-8

if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline
    # from collections import deque
    # from itertools import *
    T = int(input())
    def maxdelay(node) :
        if node in dp :
            return dp[node]
        if node not in back :
            return delay[node-1]
        else :
            maxval = 0
            for item in back[node] :
                tmp = maxdelay(item)
                if tmp > maxval :
                    maxval = tmp
            dp[node] = maxval + delay[node-1]
            return dp[node]

    for _ in range(T) :
        n, k = map(int, input().split())
        delay = list(map(int, input().split()))
        back, dp = dict(), dict()
        for i in range(k) :
            board = list(map(int, input().split()))
            if board[1] in back :
                back[board[1]].append(board[0])
            else :
                back[board[1]] = list()
                back[board[1]].append(board[0])
        goal = int(input())
        print(maxdelay(goal))
