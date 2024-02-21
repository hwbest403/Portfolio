# coding = utf-8

import sys
input = sys.stdin.readline
import bisect

T = int(input())
n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

def makesum(A) :
    ls = list()
    tmp = 0
    ls.append(tmp)
    for num in A :
        tmp += num
        ls.append(tmp)
    return ls

def prefix(A, i, j) :
    return A[j+1]-A[i]

sum_A = makesum(A)
sum_B = makesum(B)
AA = list()
for i in range(n) :
    for j in range(i, n) :
        AA.append(prefix(sum_A, i, j))
AA.sort()

ans = 0
for i in range(m) :
    for j in range(i, m) :
        l = bisect.bisect_left(AA, T-prefix(sum_B, i, j))
        r = bisect.bisect_right(AA, T-prefix(sum_B, i, j))
        ans += r-l
print(ans)