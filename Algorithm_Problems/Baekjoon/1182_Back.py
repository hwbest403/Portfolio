# coding = utf-8

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
ls = list(map(int, input().split()))

ans = 0
def backtracking(idx, res):
    global ans

    if idx >= n:
        return

    res += ls[idx]
    if res == s:
        ans += 1
    backtracking(idx+1, res)
    backtracking(idx+1, res-ls[idx])

backtracking(0, 0)
print(ans)