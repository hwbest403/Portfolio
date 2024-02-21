# https://www.acmicpc.net/problem/1026

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=False)
S = 0
for i in range(n):
    S += A[i] * B[i]
print(S)