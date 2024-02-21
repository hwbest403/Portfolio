import sys
import math
input = sys.stdin.readline

n = int(input())
board = list(map(int,input().split()))

def boardshift(n) :
    tmp = board[0]
    for i in range(n-1) :
        board[i] = board[i+1]
    board[n-1] = tmp

def prefixsum(board) :
    presum = list(0 for _ in range(len(board)))
    for idx, num in enumerate(board) :
        if idx == 0 :
            presum[idx] = num
        else :
            presum[idx] = presum[idx-1] + num
    return presum

def sol(presum, n) :
    result = 0
    for i in range(n-1) :
        if presum[i] < 0:
            result += math.ceil(-presum[i]/presum[n-1])
    return result

if __name__ == '__main__' :
    result = 0
    for _ in range(n) :
        presum = prefixsum(board)
        result += sol(presum,n)
        boardshift(n)
    print(result)