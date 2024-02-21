# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    from collections import deque
    from itertools import *

    board = list(map(int, input().split()))
    def solution(board) :
        cnum = 10000
        for i in range(4) :
            tmp = board[(0+i)%4]*1000 + board[(1+i)%4]*100 + board[(2+i)%4]*10 + board[(3+i)%4] * 1
            if tmp < cnum :
                cnum = tmp
        return cnum
    ans = solution(board)
    choice = list(product([1,2,3,4,5,6,7,8,9], repeat=4))
    arr = list()
    for i in range(len(choice)) :
        tmpcnum = solution(choice[i])
        if tmpcnum not in arr :
            arr.append(tmpcnum)
    for i in range(len(choice)) :
        if arr[i] == ans :
            print(i+1)
            break
