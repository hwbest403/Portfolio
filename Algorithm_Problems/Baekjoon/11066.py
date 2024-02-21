# coding = utf-8

import sys
input = sys.stdin.readline

def printboard(board):
    for row in board:
        print(row)

def sol():
    k = int(input())
    board = list(map(int, input().split()))
    dp = list(list(float('inf') for _ in range(k)) for _ in range(k))
    prefix_sum = list(0 for _ in range(k+1))
    for i in range(k):
        if i == 0:
            prefix_sum[i+1] = board[i]
            continue
        prefix_sum[i+1] = prefix_sum[i] + board[i]
    print(prefix_sum)
    for i in range(k):
        dp[i][i] = 0
    for len in range(1, k):
        for left in range(k-len):
            right = left+len
            for mid in range(left, right):
                dp[left][right] = min(dp[left][right], dp[left][mid]+dp[mid+1][right]+prefix_sum[right+1]-prefix_sum[left])
    printboard(dp)
    return dp[0][k-1]

T = int(input())
for _ in range(T):
    print(sol())